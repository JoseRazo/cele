from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from datetime import date as fecha_actual
from django.db.models import Count, Q, Value as V
from django.db.models.functions import Concat

from gestion_escolar.models import (
    Alumno, 
    CursoAlumno,
    Profesor
    )
from edcon.models import (
    Estudiante, 
    CursoEstudiante,
    Instructor
    )
from .models import (
    Encuesta,
    Seccion, 
    EncuestaAlumno, 
    EncuestaEstudiante, 
    RegistrosCELE, 
    RegistrosEDCON
    )

# Create your views here.
@login_required
def realizar_encuesta(request, curso_id, type):
    usuario = request.user
    grupos = request.user.groups.all()

    if type == 'AC':
        selcurso = CursoAlumno.objects.get(pk=curso_id)
    elif type == 'AE':
        selcurso = CursoEstudiante.objects.get(pk=curso_id)

    if usuario.is_superuser == 1:
            usuario_log = usuario
            status = 'admin'

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            usuario_log = Alumno.objects.get(username=usuario.username)
            selcurso = CursoAlumno.objects.get(pk=curso_id)
            log_alumno = str(selcurso.alumno)
            status = 'alumno'
        elif grupo.name == 'Estudiantes EDCON':
            usuario_log = Estudiante.objects.get(username=usuario.username)
            selcurso = CursoEstudiante.objects.get(pk=curso_id)
            log_alumno = str(selcurso.estudiante)
            status = 'estudiante'
        elif grupo.name == 'Administradores CELE' or grupo.name == 'Administradores EDCON':
            usuario_log = request.user
            status = 'admin'
        else:
            usuario_log = request.user
            return render(request, 'certificados/404.html')
    
    try:
        if status == 'alumno' or type == 'AC':
            encuesta_res = EncuestaAlumno.objects.filter(curso_alumno_id=curso_id)
            encuesta_static = RegistrosCELE.objects.filter(curso_alumno_id=curso_id)
        elif status == 'estudiante' or type == 'AE':
            encuesta_res = EncuestaEstudiante.objects.filter(curso_alumno_id=curso_id)
            encuesta_static = RegistrosEDCON.objects.filter(curso_alumno_id=curso_id)

    except ObjectDoesNotExist:
        pass

    encuesta = Encuesta.objects.get(nombre='REVIN025')
    secciones = Seccion.objects.filter(encuesta=encuesta)
    preguntas = encuesta.pregunta_set.filter(activo=True)
       
    usuario = str(request.user)

    if request.method == 'POST':
        if str(encuesta_res) == '<QuerySet []>':
            if status == 'alumno':
                registro = RegistrosCELE(
                    usuario=request.user,
                    curso_alumno=selcurso,
                    encuesta=encuesta
                )
                registro.save()
            elif status == 'estudiante':
                registro = RegistrosEDCON(
                    usuario=request.user,
                    curso_alumno=selcurso,
                    encuesta=encuesta
                )
                registro.save()

            for pregunta in preguntas:
                respuesta_texto = request.POST.get(f"pregunta_{pregunta.id}")

                if respuesta_texto:
                    if status == 'alumno':
                        solicitud_encuesta = EncuestaAlumno(
                            curso_alumno=selcurso,
                            registro=registro,
                            encuesta=encuesta,
                            pregunta=pregunta,
                            texto_respuesta=respuesta_texto
                        )
                        solicitud_encuesta.save()
                    elif status == 'estudiante':
                        solicitud_encuesta = EncuestaEstudiante(
                            curso_alumno=selcurso,
                            registro=registro,
                            encuesta=encuesta,
                            pregunta=pregunta,
                            texto_respuesta=respuesta_texto
                        )
                        solicitud_encuesta.save()

    context = {
        'selcurso': selcurso,
        'usuario_log': usuario_log, 
        'encuesta': encuesta, 
        'secciones': secciones, 
        'preguntas': preguntas, 
        'encuesta_res': encuesta_res, 
        'encuesta_static': encuesta_static, 
        'status': status
    }

    if type == 'AC' or type == 'AE':
        return render(request, 'encuestas/realizar_encuesta.html', context)
    else:
        if log_alumno == usuario:
            # El curso de alumno no pertenece al usuario logueado, mostrar un mensaje de error o redirigir a otra página
            return render(request, 'encuestas/realizar_encuesta.html', context)
        else:
            return render(request, 'certificados/curso_no_autorizado.html',
                        {'usuario_log': usuario_log})
        
    
class EncuestaAlumnoCeleListView(ListView):
    model = CursoAlumno
    context_object_name = 'encuestas'
    ordering = ['curso']
    paginate_by = 10

    def get_queryset(self):
        today = fecha_actual.today()
        queryset = CursoAlumno.objects.filter(alumno=self.request.user).order_by('-periodo__fecha_fin')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_log = Alumno.objects.get(username=self.request.user.username)
        registros = RegistrosCELE.objects.all()
        
        context['status'] = 'alumno'
        context['usuario_log'] = usuario_log
        context['registros'] = registros
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchEncuestaAlumnoCeleView(ListView):
    model = CursoAlumno
    context_object_name = 'encuestas'      # default >> erf24/post_list.html
    ordering = ['curso']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')
        today = fecha_actual.today()

        if is_valid_queryparam(search):
            obj = CursoAlumno.objects.filter(Q(curso__nombre__icontains=search, alumno=self.request.user)).distinct().order_by('-periodo__fecha_fin')

        if invalid_queryparam(search):
            obj = CursoAlumno.objects.annotate(numero_de_alumnos=Count('alumno'))
    
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_log = Alumno.objects.get(username=self.request.user.username)
        registros = RegistrosCELE.objects.all()
        
        context['status'] = 'alumno'
        context['usuario_log'] = usuario_log
        context['registros'] = registros
        return context

class EncuestaEstudianteEdconListView(ListView):
    model = CursoEstudiante
    context_object_name = 'encuestas'
    ordering = ['curso']
    paginate_by = 10

    def get_queryset(self):
        today = fecha_actual.today()
        queryset = CursoEstudiante.objects.filter(estudiante=self.request.user).order_by('-periodo__fecha_fin')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_log = Estudiante.objects.get(username=self.request.user.username)
        registros = RegistrosEDCON.objects.all()
        
        context['status'] = 'estudiante'
        context['usuario_log'] = usuario_log
        context['registros'] = registros
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchEncuestaEstudianteEdconView(ListView):
    model = CursoEstudiante
    context_object_name = 'encuestas'      # default >> erf24/post_list.html
    ordering = ['curso']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')
        today = fecha_actual.today()

        if is_valid_queryparam(search):
            obj = CursoEstudiante.objects.filter(Q(curso__nombre__icontains=search, estudiante=self.request.user)).distinct().order_by('-periodo__fecha_fin')

        if invalid_queryparam(search):
            obj = CursoEstudiante.objects.annotate(numero_de_alumnos=Count('estudiante'))
    
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_log = Estudiante.objects.get(username=self.request.user.username)
        registros = RegistrosEDCON.objects.all()
        
        context['status'] = 'estudiante'
        context['usuario_log'] = usuario_log
        context['registros'] = registros
        return context
    
class RegistroCeleListView(ListView):
    model = RegistrosCELE
    context_object_name = 'registros'
    ordering = ['curso_alumno']
    paginate_by = 10

    def get_queryset(self):
        today = fecha_actual.today()
        queryset = RegistrosCELE.objects.all().order_by('-curso_alumno__periodo__fecha_fin')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupos = self.request.user.groups.all()
        usuario = self.request.user
        
        if usuario.is_superuser == 1:
            usuario_log = usuario
            status = 'admin'

        for grupo in grupos:
            if grupo.name == 'Profesores CELE':
                usuario_log = Profesor.objects.get(username=usuario.username)
                status = 'profe'
            elif grupo.name == 'Administradores CELE':
                usuario_log = usuario
                status = 'admin'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchRegistroCeleView(ListView):
    model = RegistrosCELE
    context_object_name = 'registros'      # default >> erf24/post_list.html
    ordering = ['curso_alumno']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')
        today = fecha_actual.today()

        if is_valid_queryparam(search):
            obj = RegistrosCELE.objects.annotate(nombres=Concat('usuario__nombre', V(' '),'usuario__apellido_paterno', V(' '), 'usuario__apellido_materno')).filter(Q(curso_alumno__curso__nombre__icontains=search) | Q(nombres__icontains=search)).distinct().order_by('-curso_alumno__periodo__fecha_fin')

        if invalid_queryparam(search):
            obj = RegistrosCELE.objects.annotate(numero_de_alumnos=Count('usuario'))
    
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupos = self.request.user.groups.all()
        usuario = self.request.user

        if usuario.is_superuser == 1:
            usuario_log = usuario
            status = 'admin'
        
        for grupo in grupos:
            if grupo.name == 'Profesores CELE':
                usuario_log = Profesor.objects.get(username=usuario.username)
                status = 'profe'
            elif grupo.name == 'Administradores CELE':
                usuario_log = usuario
                status = 'admin'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        return context
    
class RegistroEdconListView(ListView):
    model = RegistrosEDCON
    context_object_name = 'registros'
    ordering = ['curso_alumno']
    paginate_by = 10

    def get_queryset(self):
        today = fecha_actual.today()
        queryset = RegistrosEDCON.objects.all().order_by('-curso_alumno__periodo__fecha_fin')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupos = self.request.user.groups.all()
        usuario = self.request.user

        if usuario.is_superuser == 1:
            usuario_log = usuario
            status = 'admin'
        
        for grupo in grupos:
            if grupo.name == 'Instructores EDCON':
                usuario_log = Instructor.objects.get(username=usuario.username)
                status = 'instru'
            elif grupo.name == 'Administradores EDCON':
                usuario_log = usuario
                status = 'admin'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None
def invalid_queryparam(param):
    return param == '' and param is None


class SearchRegistroEdconView(ListView):
    model = RegistrosEDCON
    context_object_name = 'registros'      # default >> erf24/post_list.html
    ordering = ['curso_alumno']
    paginate_by = 10

    def get_queryset(self): # new
        search = self.request.GET.get('q')
        today = fecha_actual.today()

        if is_valid_queryparam(search):
            obj = RegistrosEDCON.objects.annotate(nombres=Concat('usuario__nombre', V(' '),'usuario__apellido_paterno', V(' '), 'usuario__apellido_materno')).filter(Q(curso_alumno__curso__nombre__icontains=search) | Q(nombres__icontains=search)).distinct().order_by('-curso_alumno__periodo__fecha_fin')

        if invalid_queryparam(search):
            obj = RegistrosEDCON.objects.annotate(numero_de_alumnos=Count('usuario'))
    
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupos = self.request.user.groups.all()
        usuario = self.request.user

        if usuario.is_superuser == 1:
            usuario_log = usuario
            status = 'admin'
        
        for grupo in grupos:
            if grupo.name == 'Instructores EDCON':
                usuario_log = Instructor.objects.get(username=usuario.username)
                status = 'instru'
            elif grupo.name == 'Administradores EDCON':
                usuario_log = usuario
                status = 'admin'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        return context