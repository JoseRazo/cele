from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from gestion_escolar.models import Alumno, CursoAlumno, Periodo


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

def add_background(canvas, image_path):
    canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True, mask='auto')

# Generar PDF
def pdfgenerator(request):
    # Crea un objeto BytesIO para almacenar el PDF generado.
    buffer = BytesIO()

    # Crea un objeto canvas de ReportLab para generar el PDF.
    c = canvas.Canvas(buffer, pagesize=letter)

    # Agrega la imagen de fondo al PDF.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    STATIC_ROOT = os.path.join(BASE_DIR, "media/")
    bg_path = STATIC_ROOT + "certificados/plantilla-certificado-uts.png"
    add_background(c, bg_path)

    # Obtención de datos
    curso_alumno = CursoAlumno.objects.all().filter(alumno=request.user)

    alumno = []
    for obj in CursoAlumno.objects.all():
        alumno.append(obj.alumno)

    curso = []
    for obj in CursoAlumno.objects.all():
        curso.append(obj.curso)

    fecha_termino = []
    for obj in CursoAlumno.objects.all():
        fecha_termino.append(obj.periodo.fecha_fin)


    # Agrega contenido al PDF.
    text_nombre = str(request.user)
    text_subtitulo = str(curso)
    text_fecha = "Salamanca, Gto., a " + str(fecha_termino) 

    text_width = c.stringWidth(text_nombre, "Helvetica-Bold", 16)
    x = (letter[0] - text_width) / 2
    y = letter[1] / 2.25

    # Pasada 1: Nombre del Alumno
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(HexColor('#204089'))
    c.drawString(x, y, text_nombre)

    # Pasada 2: Motivo de la constancia
    lines = [
        "Por haber concluido satisfactoriamente el curso " + text_subtitulo,
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

    # Finaliza el PDF.
    c.showPage()
    c.save()

    # Lee los contenidos del BytesIO y devuelve una respuesta HTTP con el PDF generado.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prueba.pdf"'
    return response


# 

@login_required
def mostrar_cursos(request):
    curso_list = CursoAlumno.objects.all()

    return render(request, 'certificados/mis_cursos.html',
                  {'curso_list': curso_list}) 


 
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('certificados:dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect("certificados:dashboard")
        else:
            messages.error(request, """Por favor introduzca un nombre de usuario y
                        contraseña correctos.""")
            return redirect('certificados:login')
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

 

def logout_view(request):
    auth_logout(request)
    # Redirigir a la página de inicio o cualquier otra página deseada después del logout
    return redirect('certificados:login')

def profile_user(request):
    return render(request,"certificados/profile.html")  



@login_required
def dash_view(request):
    return render(request,"certificados/dashboard.html")





  

 



  














