from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.db.models import Count
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.db.models import Q 
from .models import Slider
from gestion_escolar.models import Curso as CursoCele
from edcon.models import Curso as CursoEdcon
from certificados.models import CertificadoAlumno
from .forms import AspiranteCeleForm, AspiranteEdconForm, ContactoForm
# Create your views here.

def home(request):
    sliders = Slider.objects.filter(activo=True)
    cursos_cele_populares = CursoCele.objects.annotate(numero_de_alumnos_cele=Count('cursoalumno')).filter(activo=True).order_by('-numero_de_alumnos_cele')[:3]
    cursos_edcon_populares = CursoEdcon.objects.annotate(numero_de_alumnos_edcon=Count('cursoestudiante')).filter(activo=True).order_by('-numero_de_alumnos_edcon')[:3]
    return render(request, "blog/home.html", {'sliders': sliders, 'cursos_cele_populares': cursos_cele_populares, 'cursos_edcon_populares': cursos_edcon_populares,})

# Views CELE
class CursoCeleListView(ListView):
    model =  CursoCele
    template_name = 'blog/cursos/cursos-cele.html'
    context_object_name = 'cursos_cele'
    ordering = ['nombre']
    paginate_by = 3

    def get_queryset(self):
        queryset = CursoCele.objects.annotate(numero_de_alumnos=Count('cursoalumno')).order_by('nombre')
        return queryset

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None

class SearchCeleView(ListView):
    model = CursoCele
    template_name = 'blog/cursos/cursos-cele.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cursos_cele'      # default >> erf24/post_list.html
    ordering = ['nombre']
    paginate_by = 3

    def get_queryset(self): # new
        search = self.request.GET.get('q')

        if is_valid_queryparam(search):
            obj = CursoCele.objects.annotate(numero_de_alumnos=Count('cursoalumno')).filter(Q(nombre__icontains=search)).distinct().order_by('nombre')

        if invalid_queryparam(search):
            obj = CursoCele.objects.annotate(numero_de_alumnos=Count('cursoalumno'))
    
        return obj

def cursoCeleDetalle(request, slug):
    curso_cele_detalle = CursoCele.objects.annotate(numero_de_alumnos=Count('cursoalumno')).filter(activo=True).get(slug=slug)
    return render(request, "blog/cursos/curso_cele_detalle.html", {'curso_cele_detalle': curso_cele_detalle,})

def formAspiranteCele(request):
    form = AspiranteCeleForm()
    status = ''
    if request.method == "POST":
        form = AspiranteCeleForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            asunto = request.POST.get('asunto')
            mensaje = request.POST.get('mensaje')
            

            email=EmailMessage("CENTRO DE LENGUAS.",
            "El usuario {} con correo electronico {} escribe lo siguiente:\n\n Asunto: {}\n\n {}".format(nombre, email, asunto, mensaje),
            "", ["celeuts@utsalamanca.edu.mx"], reply_to=[email])

            try:
                email.send()
                status = 'success'
                return HttpResponse(status)
            except Exception as e:
                status = 'error'
                return HttpResponse(status)
        else:
            status = 'errors'
            return HttpResponse(status)

# Views EDCON
class CursoEdconListView(ListView):
    model =  CursoEdcon
    template_name = 'blog/cursos/cursos-edcon.html'
    context_object_name = 'cursos_edcon'
    ordering = ['nombre']
    paginate_by = 3

    def get_queryset(self):
        queryset = CursoEdcon.objects.annotate(numero_de_estudiantes=Count('cursoestudiante')).order_by('nombre')
        return queryset

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None

class SearchEdconView(ListView):
    model = CursoEdcon
    template_name = 'blog/cursos/cursos-edcon.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cursos_edcon'      # default >> erf24/post_list.html
    ordering = ['nombre']
    paginate_by = 3

    def get_queryset(self): # new
        search = self.request.GET.get('q')
        total_cursos = CursoEdcon.objects.count()

        if is_valid_queryparam(search):
            obj = CursoEdcon.objects.annotate(numero_de_estudiantes=Count('cursoestudiante')).filter(Q(nombre__icontains=search)).distinct().order_by('nombre')

        if invalid_queryparam(search):
            obj = CursoEdcon.objects.annotate(numero_de_estudiantes=Count('cursoestudiante'))
    
        return obj

def cursoEdconDetalle(request, slug):
    curso_edcon_detalle = CursoEdcon.objects.annotate(numero_de_estudiantes=Count('cursoestudiante')).filter(activo=True).get(slug=slug)
    return render(request, "blog/cursos/curso_edcon_detalle.html", {'curso_edcon_detalle': curso_edcon_detalle,})

def formAspiranteEdcon(request):
    form = AspiranteEdconForm()
    status = ''
    if request.method == "POST":
        form = AspiranteEdconForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            asunto = request.POST.get('asunto')
            mensaje = request.POST.get('mensaje')
            

            email=EmailMessage("EDUCACIÓN CONTINUA.",
            "El usuario {} con correo electronico {} escribe lo siguiente:\n\n Asunto: {}\n\n {}".format(nombre, email, asunto, mensaje),
            "", ["mgutierrez@utsalamanca.edu.mx"], reply_to=[email])

            try:
                email.send()
                status = 'success'
                return HttpResponse(status)
            except Exception as e:
                status = 'error'
                print(e)
                return HttpResponse(status)
        else:
            status = 'errors'
            return HttpResponse(status)

def contacto(request):
    return render(request, 'blog/cursos/contacto.html')

def formContacto(request):
    form = ContactoForm()
    status = ''
    if request.method == "POST":
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            

            email=EmailMessage("FORMULARIO DE CONTACTO EDCON.",
            "El usuario {} con correo electronico {} escribe lo siguiente:\n\n Mensaje: {}".format(nombre, email, mensaje),
            "", ["celeuts@utsalamanca.edu.mx"], reply_to=[email])

            try:
                email.send()
                status = 'success'
                return HttpResponse(status)
            except Exception as e:
                status = 'error'
                print(e)
                return HttpResponse(status)
        else:
            status = 'errors'
            return HttpResponse(status)

class ValidarCertificadoListView(ListView):
    model = CertificadoAlumno
    template_name = 'blog/certificados/validar_certificado.html'
    context_object_name = 'validar_certificado'
    ordering = ['curso_alumno']
    paginate_by = 3

    def get_queryset(self):
        queryset = CertificadoAlumno.objects.filter(pk=0)
        return queryset

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None

class SearchCertificadoView(ListView):
    model = CertificadoAlumno
    template_name = 'blog/certificados/validar_certificado.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'validar_certificado'      # default >> erf24/post_list.html
    ordering = ['curso_alumno']
    paginate_by = 1

    def get_queryset(self): # new
        search = self.request.GET.get('q')

        if is_valid_queryparam(search):
            obj = CertificadoAlumno.objects.annotate(numero_de_alumnos=Count('curso_alumno')).filter(Q(folio__icontains=search)).distinct().order_by('folio')

        if invalid_queryparam(search):
            obj = CertificadoAlumno.objects.annotate(numero_de_alumnos=Count('curso_alumno'))
    
        return obj