from django.conf import settings
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.db.models import Count, Q, Value as V
from django.db.models.functions import Concat
from gestion_escolar.models import Alumno, CursoAlumno, CalificacionCurso, CalificacionCursoSemanal
from edcon.models import Estudiante, CursoEstudiante
from .models import CertificadoAlumno, CertificadoEstudiante, Plantilla
from datetime import datetime
from datetime import date as fecha_actual
import qrcode
import random
import string

import io
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.colors import blue
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import textwrap
import base64
# Create your views here.

#### Parametros de llenado: Posiciones X e Y: Declaracion de variables
param_X = []
param_Y = []

#### Parametros de llenado: Colores Hexadecimales Dinámicos (Solo usados en el nombre y subtitulo)
# [None, Nombre, Subtitulo, Fecha, Firma, Folio]
constancia_hexcolor = [None, '#204089', '#8d8989', '#9f9b9b', '#9f9b9b', '#e40e1a']
redcon_hexcolor = [None, '#000000', '#000000', '#9f9b9b', '#9f9b9b', '#e40e1a']


#Como llenar los parametros para las posiciones X e Y de los elementos del PDF: 
# [None, Nombre, Subtitulo, Fecha, Firma, Folio, QR/Sello (solo posY)]

# Parametros Constancia
constancia_X = [None, "center", "center", "center", "center", 14]
constancia_Y = [None, 352, 320, 260, 120, 55, 140]

# Parametros Constancia Red Conocer
redcon_X = [None, "center", "center", "center", "center", 14]
redcon_Y = [None, 372, 340, 280, 150, 110, 160]

# Diccionario de Meses, utilizado para traducir al español.
meses = {
    "January": "enero",
    "February": "febrero",
    "March": "marzo",
    "April": "abril",
    "May": "mayo",
    "June": "junio",
    "July": "julio",
    "August": "agosto",
    "September": "septiembre",
    "October": "octubre",
    "November": "noviembre",
    "December": "diciembre",
}
    
def add_background(canvas, image_path):
    canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True, mask='auto')

def addTextRow(canvas, txt_string, font, font_size, hex_color, posX, posY):
    text_width = canvas.stringWidth(txt_string, font, font_size)

    canvas.setFont(font, font_size)
    canvas.setFillColor(HexColor(hex_color))

    if posX == 'center':
        x = (letter[0] - text_width) / 2
    else:
        x = posX
    
    canvas.drawString(x, posY, txt_string)

def addMultipleTextRows(canvas, txt_string, wrap_char_limit, wrap_jump_size, font, font_size, hex_color, posX, initialPosY):
    canvas.setFont(font, font_size)
    canvas.setFillColor(HexColor(hex_color))

    wrapped_text = textwrap.wrap(txt_string, width=wrap_char_limit)

    y = initialPosY

    for text in wrapped_text:
        text_width = canvas.stringWidth(text, font, font_size)

        if posX == 'center':
            x = (letter[0] - text_width) / 2
        else:
            x = posX

        canvas.drawString(x, y, text)
        y -= wrap_jump_size


def add_qrcode(request, canvas, folio, posY):
    data = request.build_absolute_uri('/validar-certificado-search/?q=' + folio)
    qrimg = qrcode.make(data)
    img_name = 'qr-'+ str(folio) + str(datetime.now()) + '.png'
    img_path = '/code/media/certificados/' + img_name
    qrimg.save(img_path)

    canvas.drawImage(img_path, (letter[0] / 2) - 50, posY, width=100, height=100, preserveAspectRatio=True, mask='auto')

    os.remove(img_path)

def add_sello(canvas, posY):
    sello_path = '/code/media/sello.png'

    canvas.drawImage(sello_path, (letter[0] / 2) + 125, posY, width=100, height=100, preserveAspectRatio=True, mask='auto')

# Obtener PDF
def pdfget(request, certfolio):
    if certfolio.startswith("E"):
        curso = CertificadoEstudiante.objects.get(folio=certfolio)

        if curso.curso_alumno.curso.tipo_curso == 2:
            dynamic_hexclr = redcon_hexcolor
            param_X = redcon_X
            param_Y = redcon_Y
        else:
            dynamic_hexclr = constancia_hexcolor
            param_X = constancia_X
            param_Y = constancia_Y
        
        c_alumno = curso.curso_alumno.estudiante
    elif certfolio.startswith("C"):
        curso = CertificadoAlumno.objects.get(folio=certfolio)    
        dynamic_hexclr = constancia_hexcolor
        param_X = constancia_X
        param_Y = constancia_Y

        c_alumno = curso.curso_alumno.alumno
    
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.
    bg_path = "/code" + curso.plantilla.plantilla_sin_firma.url

    add_background(c, bg_path)
    add_qrcode(request, c, certfolio, param_Y[6])

    ############## Obtención de datos #################

# Nombre del Curso

# Fecha de Inicio y de Término
    obt_fecha = curso.curso_alumno.periodo.fecha_inicio
    fecha = ''

    for x in range(2):
        if x == 1:
            obt_fecha = curso.curso_alumno.periodo.fecha_fin
            fecha += " al "
        fecha += obt_fecha.strftime("%d")
        fecha += " de " + meses[obt_fecha.strftime("%B")]
        fecha += " del " + obt_fecha.strftime("%Y")


    ############ Agrega contenido al PDF. ##############
    text_nombre = str(c_alumno)
    text_curso =  str(curso.curso_alumno)
    text_duracion = curso.curso_alumno.curso.duracion

    text_subtitulo = (
                "Por haber concluido satisfactoriamente el curso \"" + text_curso 
                +"\" impartido en las instalaciones de la Universidad Tecnológica de Salamanca."
                )

    if certfolio.startswith("E"):
        if curso.curso_alumno.curso.tipo_curso == 2:
            text_subtitulo = (
                "Por haber culminado exitosamente el curso \"" + text_curso 
                +"\", "
                )
            if text_duracion:
                text_subtitulo += ("con una duración total de " + text_duracion + ", ")
            text_subtitulo += ("en las instalaciones de la Universidad Tecnológica de Salamanca.")
            

    text_fecha = "Salamanca, Gto., del " + str(fecha)
    text_folio = "FOLIO: " + str(certfolio)
    text_firma = str(curso.firma)

    # Pasada 1: Nombre del Alumno
    font_size = 16
    if len(text_nombre) > 35:
        font_size = 12

    addTextRow(c, text_nombre, "Helvetica-Bold", font_size, dynamic_hexclr[1], param_X[1], param_Y[1])

    # Pasada 2: Motivo de la constancia
    addMultipleTextRows(c, text_subtitulo, 80, 20, "Helvetica", 14, dynamic_hexclr[2], param_X[2], param_Y[2])

    # Pasada 3: Fecha de Término 
    addTextRow(c, text_fecha, "Helvetica", 10, dynamic_hexclr[3], param_X[3], param_Y[3])

    # Pasada 4: Firma
    addMultipleTextRows(c, text_firma, 45, 10, "Helvetica", 8, dynamic_hexclr[4], param_X[4], param_Y[4])

    # Pasada 5: Folio
    addTextRow(c, text_folio, "Helvetica", 11, dynamic_hexclr[5], param_X[5], param_Y[5])

    # Finaliza el PDF.
    c.showPage()
    c.save()

    # Lee los contenidos del BytesIO y devuelve una respuesta HTTP con el PDF generado.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + str(certfolio) + '.pdf"'
    return response

# Generar PDF
@login_required
def pdfgen(request, curso_id, firma, type):
    usuario = request.user    
    grupos = request.user.groups.all()
    status = ''
    user_isLogged = False
    autorizado = False
    calicurso = None

    for grupo in grupos:
        if grupo.name == "Alumnos CELE":
            status = 'alumno'
            user_isLogged = True

        elif grupo.name == "Estudiantes EDCON":
            status = 'estudiante'
            user_isLogged = True

        elif grupo.name == 'Administradores CELE' or grupo.name == 'Administradores EDCON' or usuario.is_superuser == 1:
            status = 'admin'

    if usuario.is_superuser == 1 or status == 'admin':
        autorizado = True

    if status == "alumno" or type == "AC" and autorizado:
        curso = CursoAlumno.objects.get(pk=curso_id)
        try:
            if curso.horario == 'Sabatino':
                calicurso = CalificacionCurso.objects.get(curso_alumno_id=curso_id)
            elif curso.horario == 'Semanal':
                calicurso = CalificacionCursoSemanal.objects.get(curso_alumno_id=curso_id)
                
            if calicurso.calificacion_final < 8.0:
                return render(request, 'certificados/requisito_no_cumplido.html',{'usuario_log': usuario, 'calicurso': calicurso})
        except ObjectDoesNotExist:
                return render(request, 'certificados/requisito_no_cumplido.html',{'usuario_log': usuario})
        status = "alumno"

        c_alumno = curso.alumno
        c_profesor = curso.profesor

        dynamic_hexclr = constancia_hexcolor
        param_X = constancia_X
        param_Y = constancia_Y

        if user_isLogged:
            if not str(request.user) == str(curso.alumno):
                return render(request, 'certificados/curso_no_autorizado.html')
            
    elif status == "estudiante" or type == "AE" and autorizado:
        curso = CursoEstudiante.objects.get(pk=curso_id)
        if curso.estatus != 2:
            return render(request, 'certificados/requisito_no_cumplido.html',{'usuario_log': usuario, 'selcurso': curso})
        status = "estudiante"

        c_alumno = curso.estudiante
        c_profesor = curso.instructor

        if curso.curso.tipo_curso == 2:
            dynamic_hexclr = redcon_hexcolor
            param_X = redcon_X
            param_Y = redcon_Y
        else:
            dynamic_hexclr = constancia_hexcolor
            param_X = constancia_X
            param_Y = constancia_Y

        if user_isLogged:
            if not str(request.user) == str(curso.estudiante):
                return render(request, 'certificados/curso_no_autorizado.html')
    
    cadena = str(c_alumno) +"|"+ str(curso.curso) +"|"+ str(c_profesor) +"|"+ str(curso.periodo) +"|"+ str(curso.periodo.fecha_inicio) +"|"+ str(curso.periodo.fecha_fin) +"|"+ str(settings.LLAVE_PRIVADA)

    firmaDigital = cadena.encode()
    firmaDigital = base64.b64encode(firmaDigital)

    digits = string.digits + string.ascii_uppercase
    result_str = ''.join(random.choice(digits) for i in range(6))

    if status == "estudiante":
        certificado_alumno = CertificadoEstudiante.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

        if certificado_alumno:
            folio = certificado_alumno.folio
            bg_path = certificado_alumno
        else:
            ultimo_folio = CertificadoEstudiante.objects.last()
            if not ultimo_folio:
                now = datetime.now()
                folio = "E" + now.strftime("%y") +'-'+ result_str + '-0001'
            else:
                now = datetime.now()
                folio_anterior = int(ultimo_folio.folio.split('-')[-1])
                consecutivo = folio_anterior + 1
                folio = 'E' + now.strftime("%y") + '-'+ result_str +'-'+ str(consecutivo).zfill(4)

            # Crea un nuevo registro en CertificadoAlumno con el folio generado

            if curso.curso.tipo_curso == 2:
                certificado_alumno = CertificadoEstudiante.objects.create(
                    curso_alumno_id=curso_id,
                    plantilla = Plantilla.objects.filter(tipo_plantilla='Constancia Red Conocer').last(),
                    folio=folio,
                    firma=firmaDigital,
                    cadena = cadena
                )
            else:
                certificado_alumno = CertificadoEstudiante.objects.create(
                curso_alumno_id=curso_id,
                plantilla = Plantilla.objects.filter(tipo_plantilla='Constancia UTS').last(),
                folio=folio,
                firma=firmaDigital,
                cadena = cadena
            )
            bg_path = CertificadoEstudiante.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

    elif status == "alumno":
        certificado_alumno = CertificadoAlumno.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

        if certificado_alumno:
            folio = certificado_alumno.folio
            bg_path = certificado_alumno
        else:
            ultimo_folio = CertificadoAlumno.objects.last()
            if not ultimo_folio:
                now = datetime.now()
                folio = 'C' + now.strftime("%y") +'-'+ result_str + '-0001'
            else:
                now = datetime.now()
                folio_anterior = int(ultimo_folio.folio.split('-')[-1])
                consecutivo = folio_anterior + 1
                folio = 'C' + now.strftime("%y") + '-'+ result_str +'-'+ str(consecutivo).zfill(4)

            certificado_alumno = CertificadoAlumno.objects.create(
                curso_alumno_id=curso_id,
                plantilla = Plantilla.objects.filter(tipo_plantilla='Constancia UTS').last(),
                folio=folio,
                firma=firmaDigital,
                cadena = cadena
            )
            bg_path = CertificadoAlumno.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

    
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.
    plantilla_path = "/code" + bg_path.plantilla.plantilla_sin_firma.url
    firma_path = "/code" + bg_path.plantilla.plantilla_con_firma.url

    if firma == 'False':
        add_background(c, plantilla_path)
        add_qrcode(request, c, folio, param_Y[6])

    if str(firma) == 'cfdr':
        add_background(c, firma_path)
        add_sello(c, param_Y[6])

    ############## Obtención de datos #################

    # Obtenemos la fecha de inicio y fin del curso
    obt_fecha = certificado_alumno.curso_alumno.periodo.fecha_inicio
    fecha = ''

    for x in range(2):
        if x == 1:
            obt_fecha = certificado_alumno.curso_alumno.periodo.fecha_fin
            fecha += " al "
        fecha += obt_fecha.strftime("%d")
        fecha += " de " + meses[obt_fecha.strftime("%B")]
        fecha += " del " + obt_fecha.strftime("%Y")

    ############ Agrega contenido al PDF. ##############
    text_nombre = str(c_alumno)
    text_curso =  str(certificado_alumno.curso_alumno)
    text_duracion =certificado_alumno.curso_alumno.curso.duracion

    text_subtitulo = (
                "Por haber concluido satisfactoriamente el curso \"" + text_curso 
                +"\" impartido en las instalaciones de la Universidad Tecnológica de Salamanca."
                )

    if status == 'estudiante' or type == 'AE' and autorizado:
        if certificado_alumno.curso_alumno.curso.tipo_curso == 2:
            text_subtitulo = (
                "Por haber culminado exitosamente el curso \"" + text_curso 
                +"\", "
                )
            if text_duracion:
                text_subtitulo += ("con una duración total de " + text_duracion + ", ")
            text_subtitulo += ("en las instalaciones de la Universidad Tecnológica de Salamanca.")

    text_fecha = "Salamanca, Gto., del " + str(fecha)
    text_folio = "FOLIO: " + str(folio)

    # Pasada 1: Nombre del Alumno
    font_size = 16
    if len(text_nombre) > 35:
        font_size = 12

    addTextRow(c, text_nombre, "Helvetica-Bold", font_size, dynamic_hexclr[1], param_X[1], param_Y[1])

    # Pasada 2: Motivo de la constancia
    addMultipleTextRows(c, text_subtitulo, 80, 20, "Helvetica", 14, dynamic_hexclr[2], param_X[2], param_Y[2])

    # Pasada 3: Fecha de Término 
    addTextRow(c, text_fecha, "Helvetica", 10, dynamic_hexclr[3], param_X[3], param_Y[3])

    # Pasada 4: Firma
    if firma == 'False':
        addMultipleTextRows(c, str(firmaDigital), 45, 10, "Helvetica", 8, dynamic_hexclr[4], param_X[4], param_Y[4])

    # Pasada 5: Folio
    addTextRow(c, text_folio, "Helvetica", 11, dynamic_hexclr[5], param_X[5], param_Y[5])
    
    # Finaliza el PDF.
    c.showPage()
    c.save()

    # Lee los contenidos del BytesIO y devuelve una respuesta HTTP con el PDF generado.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + str(folio) + '.pdf"'
    return response

@login_required
def no_autorizado(request):
    usuario_log = request.user
    status = "null"
    return render(request, 'certificados/curso_no_autorizado.html', {'usuario_log': usuario_log, 'status': status})

@login_required
def listar_cursos(request):
    today = fecha_actual.today()
    usuario = request.user
    curso_list = []
    grupos = request.user.groups.all()
    today = fecha_actual.today()
    

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            usuario_log = Alumno.objects.get(username=usuario.username)
            curso_list = CursoAlumno.objects.filter(alumno=usuario)
            status = 'alumno'
        elif grupo.name == 'Estudiantes EDCON':
            usuario_log = Estudiante.objects.get(username=usuario.username)
            curso_list = CursoEstudiante.objects.filter(estudiante=usuario) 
            status = 'estudiante'
        else:
            usuario_log = request.user
            return render(request, 'certificados/404.html', {'usuario_log': usuario_log})

    return render(request, 'certificados/mis_cursos.html', {'curso_list': curso_list, 'usuario_log': usuario_log, 'today': today, 'status': status}) 

@login_required
def mostrar_curso(request, curso_id):
    usuario = request.user
    grupos = request.user.groups.all()
    calicurso = None

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            usuario_log = Alumno.objects.get(username=usuario.username)
            selcurso = CursoAlumno.objects.get(pk=curso_id)
            status = 'alumno'
            if selcurso:
                try:
                    if selcurso.horario == 'Sabatino':
                        calicurso = CalificacionCurso.objects.get(curso_alumno_id=curso_id)
                    elif selcurso.horario == 'Semanal':
                        calicurso = CalificacionCursoSemanal.objects.get(curso_alumno_id=curso_id)
                except ObjectDoesNotExist:
                    pass
            log_alumno = str(selcurso.alumno)
        elif grupo.name == 'Estudiantes EDCON':
            usuario_log = Estudiante.objects.get(username=usuario.username)
            selcurso = CursoEstudiante.objects.get(pk=curso_id)
            log_alumno = str(selcurso.estudiante)
            status = 'estudiante'
        else:
            usuario_log = request.user
            return render(request, 'certificados/404.html')
        
    usuario = str(request.user)

    if log_alumno == usuario:
        # El curso de alumno no pertenece al usuario logueado, mostrar un mensaje de error o redirigir a otra página
        return render(request, 'certificados/mis_cursos_detail.html', 
                  {'selcurso': selcurso, 'usuario_log': usuario_log, 'calicurso': calicurso, 'status': status})
    else:
        return render(request, 'certificados/curso_no_autorizado.html',
                      {'usuario_log': usuario_log})

class CursosAlumnoCeleListView(ListView):
    model = CursoAlumno
    # template_name = 'blog/certificados/certi-cele.html'
    context_object_name = 'cursos_cele'
    ordering = ['alumno']
    paginate_by = 10

    def get_queryset(self):
        queryset = CursoAlumno.objects.filter(Q(horario='Sabatino', calicurso__calificacion_final__gte=8.0) | Q(horario='Semanal', calicursosem__calificacion_final__gte=8.0)).order_by('alumno')
        return queryset
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(CursosAlumnoCeleListView, self).get(*args, **kwargs)

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchCursosAlumnoCeleView(ListView):
    model = CursoAlumno
    # template_name = 'blog/certificados/certi-cele.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cursos_cele'      # default >> erf24/post_list.html
    ordering = ['alumno']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')

        if is_valid_queryparam(search):
            obj = CursoAlumno.objects.annotate(
                nombres=Concat('alumno__nombre', V(' '),  'alumno__apellido_paterno', V(' '),'alumno__apellido_materno'
                )).filter(
                Q(nombres__icontains=search, horario='Sabatino', calicurso__calificacion_final__gte=8.0) | Q(alumno__username__icontains=search, horario='Sabatino', calicurso__calificacion_final__gte=8.0) |
                Q(nombres__icontains=search, horario='Semanal', calicursosem__calificacion_final__gte=8.0) | Q(alumno__username__icontains=search, horario='Semanal', calicursosem__calificacion_final__gte=8.0)
                ).distinct().order_by('periodo')

        if invalid_queryparam(search):
            obj = CursoAlumno.objects.annotate(numero_de_alumnos=Count('alumno'))
    
        return obj
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchCursosAlumnoCeleView, self).get(*args, **kwargs)


class CursosEstudianteEdconListView(ListView):
    model = CursoEstudiante
    # template_name = 'blog/certificados/certi-cele.html'
    context_object_name = 'cursos_edcon'
    ordering = ['estudiante']
    paginate_by = 10

    def get_queryset(self):
        queryset = CursoEstudiante.objects.filter(estatus=2).order_by('estudiante')
        return queryset
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(CursosEstudianteEdconListView, self).get(*args, **kwargs)

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchCursosEstudianteEdconView(ListView):
    model = CursoEstudiante
    # template_name = 'blog/certificados/certi-cele.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cursos_edcon'      # default >> erf24/post_list.html
    ordering = ['estudiante']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')

        if is_valid_queryparam(search):
            obj = CursoEstudiante.objects.annotate(nombres=Concat('estudiante__nombre', V(' '),'estudiante__apellido_paterno', V(' '), 'estudiante__apellido_materno')).filter(Q(nombres__icontains=search, estatus=2) | Q(estudiante__username__icontains=search, estatus=2)).distinct().order_by('estudiante')

        if invalid_queryparam(search):
            obj = CursoEstudiante.objects.annotate(numero_de_alumnos=Count('estudiante'))
    
        return obj
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchCursosEstudianteEdconView, self).get(*args, **kwargs)