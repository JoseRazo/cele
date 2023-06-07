from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.db.models import Count, Q 
from .forms import LoginForm
from edcon.models import Curso as Curso2
from gestion_escolar.models import Alumno, CursoAlumno, Periodo, Curso
from edcon.models import Estudiante, CursoEstudiante, Periodo
from .models import CertificadoAlumno, CertificadoEstudiante, Plantilla
from datetime import datetime
from usuarios.models import Usuario
from datetime import date as fecha_actual
import qrcode
import random
import string


from django.http import FileResponse
import io
from pathlib import Path
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

def add_background(canvas, image_path):
    canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True, mask='auto')

def add_qrcode(canvas, folio):
    data = "http://127.0.0.1:8000/validar-certificado-search/?q=" + folio
    qrimg = qrcode.make(data)
    img_name = 'qr-'+ str(folio) + str(datetime.now()) + '.png'
    img_path = '/code/media/certificados/' + img_name
    qrimg.save(img_path)

    canvas.drawImage(img_path, (letter[0] / 2) - 50, letter[1] / 6, width=100, height=100, preserveAspectRatio=True, mask='auto')

    os.remove(img_path)

# Generar PDF

def pdfget(request, certfolio):
    if certfolio.startswith("E"):
        curso = CertificadoEstudiante.objects.get(folio=certfolio)
        print("usuario edcon")
        
        c_alumno = curso.curso_alumno.estudiante
    elif certfolio.startswith("C"):
        curso = CertificadoAlumno.objects.get(folio=certfolio)    
        print("usuario cele")

        c_alumno = curso.curso_alumno.alumno
    
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.
    bg_path = "/code" + curso.plantilla.imagen.url

    print(bg_path)

    add_background(c, bg_path)

    add_qrcode(c, certfolio)

    ############## Obtención de datos #################

# Nombre del Curso

# Fecha de Inicio y de Término
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

    fecha = curso.curso_alumno.periodo.fecha_inicio.strftime("%d")
    fecha += " de " + meses[curso.curso_alumno.periodo.fecha_inicio.strftime("%B")]
    fecha += " del " + curso.curso_alumno.periodo.fecha_inicio.strftime("%Y")
    fecha += " al " + curso.curso_alumno.periodo.fecha_fin.strftime("%d")
    fecha += " de " + meses[curso.curso_alumno.periodo.fecha_fin.strftime("%B")]
    fecha += " del " + curso.curso_alumno.periodo.fecha_fin.strftime("%Y")


    ############ Agrega contenido al PDF. ##############
    text_nombre = str(c_alumno)
    text_subtitulo =  str(curso.curso_alumno.curso)
    text_fecha = "Salamanca, Gto., del " + str(fecha)
    text_folio = "FOLIO: " + str(certfolio)
    text_firma = str(curso.firma)


    text_width = c.stringWidth(text_nombre, "Helvetica-Bold", 16)
    x = (letter[0] - text_width) / 2
    y = letter[1] / 2.25

    # Pasada 1: Nombre del Alumno
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(HexColor('#204089'))
    c.drawString(x, y, text_nombre)

    # Pasada 2: Motivo de la constancia
    lines = [
        "Por haber concluido satisfactoriamente el curso \"" + text_subtitulo +"\"",
        "impartido en las instalaciones de la Universidad Tecnológica de Salamanca."
    ]
    
    textob = c.beginText()

    text_width = c.stringWidth(lines[0], "Helvetica", 14)
    x = (letter[0] - text_width) / 2

    textob.setTextOrigin(x, (letter[1] / 2.5))
    textob.setFont("Helvetica", 14)
    textob.setFillColor(HexColor('#8d8989'))
    for line in lines:
        textob.textLine(line)
        c.drawText(textob)
        text_width = c.stringWidth(lines[1], "Helvetica", 14)
        x = (letter[0] - text_width) / 2
        textob.setTextOrigin(x, (letter[1] / 2.65))

    # Pasada 3: Fecha de Término 
    text_width = c.stringWidth(text_fecha, "Helvetica", 10)
    x = (letter[0] - text_width) / 2
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor('#9f9b9b'))
    c.drawString(x, (letter[1] / 3.04), text_fecha)

    # Pasada 4: Folio
    text_width = c.stringWidth(text_fecha, "Helvetica", 11)
    x = 14
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor('#e40e1a'))
    c.drawString(x, (letter[1] / 14.05), text_folio)

    # Pasada 5: Firma
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor('#9f9b9b'))

    if len(text_firma) > 45:
        wrap_text = textwrap.wrap(str(text_firma), width=45)
        y = 120
        pos = 0
        for i in wrap_text:
            text_width = c.stringWidth(wrap_text[pos], "Helvetica", 8)
            x = (letter[0] - text_width) / 2
            c.drawString(x, y, wrap_text[pos])
            y -= 10
            print(y)
            pos = pos + 1
    else:
        text_width = c.stringWidth(text_firma, "Helvetica", 8)
        x = (letter[0] - text_width) / 2
        c.drawString(x, (letter[1] / 12.05), text_firma)
        

    # Finaliza el PDF.
    c.showPage()
    c.save()

    # Lee los contenidos del BytesIO y devuelve una respuesta HTTP con el PDF generado.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prueba.pdf"'
    return response


@login_required
def pdfgen(request, curso_id, firma, type):
    print(settings.LLAVE_PRIVADA)
    usuario = request.user    
    filtro = str(Alumno.objects.filter(username=usuario.username))

    if usuario.is_staff == 1:
        if type == "AC":
            curso = CursoAlumno.objects.get(pk=curso_id)
            filtro = "Alumno"

            c_alumno = curso.alumno
            c_profesor = curso.profesor
        elif type == "AE":
            curso = CursoEstudiante.objects.get(pk=curso_id)
            filtro = "<QuerySet []>"

            c_alumno = curso.estudiante
            c_profesor = curso.instructor
    else:
        if filtro == "<QuerySet []>":
            curso = CursoEstudiante.objects.get(pk=curso_id)
            print("usuario edcon")

            if not str(request.user) == str(curso.estudiante):
                return render(request, 'certificados/curso_no_autorizado.html')
            
            c_alumno = curso.estudiante
            c_profesor = curso.instructor
        else:
            curso = CursoAlumno.objects.get(pk=curso_id)    
            print("usuario cele")

            if not str(request.user) == str(curso.alumno):
                return render(request, 'certificados/curso_no_autorizado.html')

            c_alumno = curso.alumno
            c_profesor = curso.profesor
    
    cadena = str(c_alumno) +"|"+ str(curso.curso) +"|"+ str(c_profesor) +"|"+ str(curso.periodo) +"|"+ str(curso.periodo.fecha_inicio) +"|"+ str(curso.periodo.fecha_fin) +"|"+ str(settings.LLAVE_PRIVADA)

    firmaDigital = cadena.encode()
    firmaDigital = base64.b64encode(firmaDigital)

    digits = string.digits + string.ascii_uppercase
    result_str = ''.join(random.choice(digits) for i in range(6))

    if filtro == "<QuerySet []>":
        certificado_alumno = CertificadoEstudiante.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

        if certificado_alumno:
            folio = certificado_alumno.folio
            print(folio)
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
            certificado_alumno = CertificadoEstudiante.objects.create(
                curso_alumno_id=curso_id,
                plantilla = Plantilla.objects.filter(firma_rector=False).last(),
                folio=folio,
                firma=firmaDigital,
                cadena = cadena
            )
        bg_path = CertificadoEstudiante.objects.last()
    else:
        certificado_alumno = CertificadoAlumno.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

        if certificado_alumno:
            folio = certificado_alumno.folio
            print(folio)
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
                plantilla = Plantilla.objects.filter(firma_rector=False).last(),
                folio=folio,
                firma=firmaDigital,
                cadena = cadena
            )

        bg_path = CertificadoAlumno.objects.last()
    


    print(folio)

    print(certificado_alumno)
    
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.
    bg_path = "/code" + bg_path.plantilla.imagen.url

    print(bg_path)

    add_background(c, bg_path)

    if firma == 'False':
        add_qrcode(c, folio)

    if firma == 'True':
        firma_path = Plantilla.objects.filter(firma_rector=True).last()
        image_path = "/code" + firma_path.imagen.url 
        c.drawImage(image_path, 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True, mask='auto')

    ############## Obtención de datos #################

    # Nombre del Curso

    # Fecha de Inicio y de Término
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

    fecha = certificado_alumno.curso_alumno.periodo.fecha_inicio.strftime("%d")
    fecha += " de " + meses[certificado_alumno.curso_alumno.periodo.fecha_inicio.strftime("%B")]
    fecha += " del " + certificado_alumno.curso_alumno.periodo.fecha_inicio.strftime("%Y")
    fecha += " al " + certificado_alumno.curso_alumno.periodo.fecha_fin.strftime("%d")
    fecha += " de " + meses[certificado_alumno.curso_alumno.periodo.fecha_fin.strftime("%B")]
    fecha += " del " + certificado_alumno.curso_alumno.periodo.fecha_fin.strftime("%Y")

    ############ Agrega contenido al PDF. ##############
    text_nombre = str(c_alumno)
    text_subtitulo =  str(certificado_alumno.curso_alumno)
    text_fecha = "Salamanca, Gto., del " + str(fecha)
    text_folio = "FOLIO: " + str(folio)

    # Recordar de escalar la fuente del nombre acorde al tamaño del string
    text_width = c.stringWidth(text_nombre, "Helvetica-Bold", 16)
    x = (letter[0] - text_width) / 2
    y = letter[1] / 2.25

    # Pasada 1: Nombre del Alumno
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(HexColor('#204089'))
    c.drawString(x, y, text_nombre)

    # Pasada 2: Motivo de la constancia
    lines = [
        "Por haber concluido satisfactoriamente el curso \"" + text_subtitulo +"\"",
        "impartido en las instalaciones de la Universidad Tecnológica de Salamanca."
    ]
    
    textob = c.beginText()

    text_width = c.stringWidth(lines[0], "Helvetica", 14)
    x = (letter[0] - text_width) / 2

    textob.setTextOrigin(x, (letter[1] / 2.5))
    textob.setFont("Helvetica", 14)
    textob.setFillColor(HexColor('#8d8989'))
    for line in lines:
        textob.textLine(line)
        c.drawText(textob)
        text_width = c.stringWidth(lines[1], "Helvetica", 14)
        x = (letter[0] - text_width) / 2
        textob.setTextOrigin(x, (letter[1] / 2.65))

    # Pasada 3: Fecha de Término 
    text_width = c.stringWidth(text_fecha, "Helvetica", 10)
    x = (letter[0] - text_width) / 2
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor('#9f9b9b'))
    c.drawString(x, (letter[1] / 3.04), text_fecha)

    # Pasada 4: Folio
    text_width = c.stringWidth(text_fecha, "Helvetica", 11)
    x = 14
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor('#e40e1a'))
    c.drawString(x, (letter[1] / 14.05), text_folio)

    # Pasada 5: Firma}

    if firma == 'False':
        c.setFont("Helvetica", 8)
        c.setFillColor(HexColor('#9f9b9b'))

        if len(firmaDigital) > 45:
            wrap_text = textwrap.wrap(str(firmaDigital), width=45)
            y = 120
            pos = 0
            for i in wrap_text:
                text_width = c.stringWidth(wrap_text[pos], "Helvetica", 8)
                x = (letter[0] - text_width) / 2
                c.drawString(x, y, wrap_text[pos])
                y -= 10
                print(y)
                pos = pos + 1
        else:
            text_width = c.stringWidth(firmaDigital, "Helvetica", 8)
            x = (letter[0] - text_width) / 2
            c.drawString(x, (letter[1] / 12.05), firmaDigital)
    
        

    # Finaliza el PDF.
    c.showPage()
    c.save()

    # Lee los contenidos del BytesIO y devuelve una respuesta HTTP con el PDF generado.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prueba.pdf"'
    return response


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
        elif grupo.name == 'Estudiantes EDCON':
            usuario_log = Estudiante.objects.get(username=usuario.username)
            curso_list = CursoEstudiante.objects.filter(estudiante=usuario) 
        else:
            usuario_log = request.user

    return render(request, 'certificados/mis_cursos.html', {'curso_list': curso_list, 'usuario_log': usuario_log, 'today': today}) 


@login_required
def mostrar_curso(request, curso_id):
    usuario = request.user
    grupos = request.user.groups.all()

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            usuario_log = Alumno.objects.get(username=usuario.username)
            selcurso = CursoAlumno.objects.get(pk=curso_id)
            log_alumno = str(selcurso.alumno)
        elif grupo.name == 'Estudiantes EDCON':
            usuario_log = Estudiante.objects.get(username=usuario.username)
            selcurso = CursoEstudiante.objects.get(pk=curso_id)
            log_alumno = str(selcurso.estudiante)
        else:
            usuario_log = request.user
            return render(request, 'certificados/404.html')
        
    usuario = str(request.user)

    if log_alumno == usuario:
        # El curso de alumno no pertenece al usuario logueado, mostrar un mensaje de error o redirigir a otra página
        return render(request, 'certificados/mis_cursos_detail.html', 
                  {'selcurso': selcurso, 'usuario_log': usuario_log})
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
        queryset = CursoAlumno.objects.annotate(numero_de_alumnos=Count('alumno')).order_by('alumno')
        return queryset

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
            obj = CursoAlumno.objects.annotate(numero_de_alumnos=Count('alumno')).filter(Q(alumno__nombre__icontains=search) | Q(alumno__username__icontains=search)).distinct().order_by('alumno')

        if invalid_queryparam(search):
            obj = CursoAlumno.objects.annotate(numero_de_alumnos=Count('alumno'))
    
        return obj


class CursosEstudianteEdconListView(ListView):
    model = CursoEstudiante
    # template_name = 'blog/certificados/certi-cele.html'
    context_object_name = 'cursos_edcon'
    ordering = ['estudiante']
    paginate_by = 10

    def get_queryset(self):
        queryset = CursoEstudiante.objects.annotate(numero_de_alumnos=Count('estudiante')).order_by('estudiante')
        return queryset

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
            obj = CursoEstudiante.objects.annotate(numero_de_alumnos=Count('estudiante')).filter(Q(estudiante__nombre__icontains=search) | Q(estudiante__username__icontains=search)).distinct().order_by('estudiante')

        if invalid_queryparam(search):
            obj = CursoEstudiante.objects.annotate(numero_de_alumnos=Count('estudiante'))
    
        return obj