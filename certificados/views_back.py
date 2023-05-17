from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm
from gestion_escolar.models import Alumno, CursoAlumno, Periodo
from .models import CertificadoAlumno, Plantilla
from datetime import datetime
from usuarios.models import Usuario

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
import base64
# Create your views here.

def incrementarFolio():
    # if not ultimo_folio:
    now = datetime.now()
    folio_def = now.strftime("%y") + '-0001'
    return folio_def
    # num_folio = ultimo_folio.folio
    # int_folio = int(num_folio.split("-")[-1])
    # nuevo_int_folio = int_folio + 1
    # nuevo_int_folio = '{0:04d}'.format(nuevo_int_folio)
    # nuevo_int_folio = ultimo_folio.curso_alumno.periodo.fecha_fin.strftime("%y") +"-"+ str(nuevo_int_folio)
    # return nuevo_int_folio
    

def add_background(canvas, image_path):
    canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True, mask='auto')

# Generar PDF
@login_required
def pdfgen(request, curso_id, firma):
    curso = CursoAlumno.objects.get(pk=curso_id)

    cadena = str(curso.alumno) +"|"+ str(curso.curso) +"|"+ str(curso.profesor) +"|"+ str(curso.periodo) +"|"+ str(curso.periodo.fecha_inicio) +"|"+ str(curso.periodo.fecha_fin) +"|"+ str(curso.curso.duracion) +"|"
    cadena += str(curso.inscrito) +"|"+ str(curso.curso.precio_estudiante_uts) +"|"+ str(curso.curso.precio_persona_externa)# +"|"+ str(cali.primer_examen) +"|"+ str(cali.segundo_examen) +"|"+ str(cali.calificacion_final)

    firmaDigital = cadena.encode()
    firmaDigital = base64.b64encode(firmaDigital)

    certificado_alumno = CertificadoAlumno.objects.filter(curso_alumno_id=curso_id, firma=firmaDigital).first()

    if certificado_alumno:
        folio = certificado_alumno.folio
        print(folio)
    else:
        ultimo_folio = CertificadoAlumno.objects.last()
        if not ultimo_folio:
            now = datetime.now()
            folio = now.strftime("%y") + '-0001'
        else:
            now = datetime.now()
            folio_anterior = int(ultimo_folio.folio.split('-')[-1])
            consecutivo = folio_anterior + 1
            folio = now.strftime("%y") + '-' + str(consecutivo).zfill(4)

        # Crea un nuevo registro en CertificadoAlumno con el folio generado
        certificado_alumno = CertificadoAlumno.objects.create(
            curso_alumno_id=curso_id,
            plantilla = Plantilla.objects.last(),
            folio=folio,
            firma=firmaDigital,
            cadena = cadena
            )
        print(folio)

    print(certificado_alumno)
    
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.

    # BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    # STATIC_ROOT = os.path.join(BASE_DIR, "media/")
    
    # if firma == 'True':    
    #     bg_path = STATIC_ROOT + "certificados/plantilla-certificado-uts.png"
    # else:
    #     bg_path = STATIC_ROOT + "certificados/plantilla-certificado-uts_nofirma.png"

    bg_path = CertificadoAlumno.objects.last()

    bg_path = "/code" + bg_path.plantilla.imagen.url

    print(bg_path)

    add_background(c, bg_path)

    ############## Obtención de datos #################

# Nombre del Curso
    curso = CursoAlumno.objects.get(pk=curso_id)
    # cali = CalificacionCurso.objects.get(pk=curso_id)

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

    fecha = curso.periodo.fecha_inicio.strftime("%d")
    fecha += " de " + meses[curso.periodo.fecha_inicio.strftime("%B")]
    fecha += " del " + curso.periodo.fecha_inicio.strftime("%Y")
    fecha += " al " + curso.periodo.fecha_fin.strftime("%d")
    fecha += " de " + meses[curso.periodo.fecha_fin.strftime("%B")]
    fecha += " del " + curso.periodo.fecha_fin.strftime("%Y")

    folio = ""


    ############ Agrega contenido al PDF. ##############
    text_nombre = str(request.user)
    text_subtitulo =  str(curso)
    text_fecha = "Salamanca, Gto., del " + str(fecha)
    text_folio = "FOLIO: " + str(folio)


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
    usuario = request.user
    curso_list = CursoAlumno.objects.filter(alumno=usuario)
   

    return render(request, 'certificados/mis_cursos.html',
                  {'curso_list': curso_list}) 

@login_required
def mostrar_curso(request, curso_id):
    selcurso = get_object_or_404(CursoAlumno, id=curso_id)

    # Verificar si el curso de alumno pertenece al usuario logueado
    if selcurso.usuario != request.user:
        # El curso de alumno no pertenece al usuario logueado, mostrar un mensaje de error o redirigir a otra página
        return render(request, 'certificados/curso_no_autorizado.html')
    
    return render(request, 'certificados/mis_cursos_detail.html', 
                  {'selcurso': selcurso})

  

 



  













