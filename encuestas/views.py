import xlwt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from datetime import date as fecha_actual
from django.db.models import Count, Q, Value as V
from django.db.models.functions import Concat
from django.http import HttpResponse

from gestion_escolar.models import (
    Alumno, 
    Curso as CursoCELE,
    CursoAlumno,
    Profesor,
    Periodo as PeriodoCELE
    )
from edcon.models import (
    Curso as CursoEDCON,
    Estudiante, 
    CursoEstudiante,
    Instructor,
    Periodo as PeriodoEDCON
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

@login_required
def reportgen(request, type):
    try:
        grupos = request.user.groups.all()
        for grupo in grupos :
            if grupo.name == 'Administradores CELE' or grupo.name == 'Administradores EDCON' or request.user.is_superuser == 1:
                status = 'admin'
            else:
                return render(request, 'certificados/404.html')
        
        filename = ''
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Reporte')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        selcurso = request.GET.get('curso')
        selprofe = request.GET.get('profe')
        selperiodo = request.GET.get('periodo')

        if not selcurso and not selprofe and not selperiodo:
            messages.error(request, 'Selecciona al menos 1 filtro.')
            if type == "AC":
                return redirect('/reportes-cele')
            elif type == "AE":
                return redirect('/reportes-edcon')

        filtros = {}

        if selcurso:
            filtros['curso_alumno__curso__nombre'] = selcurso
            filename += '_' + str(selcurso)
        if selprofe:
            filtros['nombres'] = selprofe
            filename += '_' + str(selprofe)
        if selperiodo:
            filtros['curso_alumno__periodo'] = selperiodo
            filename += '_' + str(selperiodo)

        if type == "AC":
            selreporte = RegistrosCELE.objects.annotate(nombres=Concat('curso_alumno__profesor__nombre', V(' '),'curso_alumno__profesor__apellido_paterno', V(' '), 'curso_alumno__profesor__apellido_materno')).filter(**filtros)
            reporte_type = "CELE"
        elif type == "AE":
            selreporte = RegistrosEDCON.objects.annotate(nombres=Concat('curso_alumno__instructor__nombre', V(' '),'curso_alumno__instructor__apellido_paterno', V(' '), 'curso_alumno__instructor__apellido_materno')).filter(**filtros)
            reporte_type = "EDCON"

        encuesta = selreporte[0].encuesta
        get_preguntas = encuesta.pregunta_set.filter(activo=True)
        preguntas = []
        for pregunta in get_preguntas:
            preguntas.append(pregunta.texto_pregunta)

        datos = []

        columns = ["Curso", "Alumno/Estudiante", "Profesor", "Periodo"]
        columns.extend(preguntas)


        for col_num, col in enumerate(columns):
            ws.write(row_num, col_num, col, font_style)
            cwidth = ws.col(col_num).width
            if (len(col)*367) > cwidth:  
                ws.col(col_num).width = len(col)*300
        
        
        font_style = xlwt.XFStyle()

        for index, obj in enumerate(selreporte):
            if type == "AC":
                encuestas = EncuestaAlumno.objects.annotate(nombres=Concat('curso_alumno__profesor__nombre', V(' '),'curso_alumno__profesor__apellido_paterno', V(' '), 'curso_alumno__profesor__apellido_materno')).filter(**filtros)
            elif type == "AE":
                encuestas = EncuestaEstudiante.objects.annotate(nombres=Concat('curso_alumno__instructor__nombre', V(' '),'curso_alumno__instructor__apellido_paterno', V(' '), 'curso_alumno__instructor__apellido_materno')).filter(**filtros)

            respuestas = []
            for enc in encuestas:
                if type == "AC":
                    if enc.curso_alumno.curso == selreporte[index].curso_alumno.curso and enc.curso_alumno.alumno == selreporte[index].curso_alumno.alumno:
                        respuestas.append(enc.texto_respuesta)
                elif type == "AE":
                    if enc.curso_alumno.curso == selreporte[index].curso_alumno.curso and enc.curso_alumno.estudiante == selreporte[index].curso_alumno.estudiante:
                        respuestas.append(enc.texto_respuesta)

            datos = [str(obj.curso_alumno)]
            datos.append(str(obj.usuario))
            if type == "AC":
                datos.append(str(obj.curso_alumno.profesor))
            elif type == "AE":
                datos.append(str(obj.curso_alumno.instructor))
            datos.append(str(obj.curso_alumno.periodo))
            datos.extend(respuestas)

            for col_num, dato in enumerate(datos):
                ws.write(index + 1, col_num, dato, font_style)


        today = fecha_actual.today()
        filename = 'attachment; filename="Reporte' + reporte_type + filename + '_' + str(today) + '.xls"'
        response = HttpResponse(
            content_type='application/ms-excel',
            headers={"Content-Disposition": filename}
            )

        wb.save(response)

        return response
    except:
        messages.error(request, 'No existen registros que cumplan con los filtros seleccionados.')
        if type == "AC":
            return redirect('/reportes-cele')
        elif type == "AE":
            return redirect('/reportes-edcon')


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
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Alumnos CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(EncuestaAlumnoCeleListView, self).get(*args, **kwargs)

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
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Alumnos CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchEncuestaAlumnoCeleView, self).get(*args, **kwargs)

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
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Estudiantes EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(EncuestaEstudianteEdconListView, self).get(*args, **kwargs)

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
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Estudiantes EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchEncuestaEstudianteEdconView, self).get(*args, **kwargs)

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
        usuario_log = usuario

        cursos = CursoCELE.objects.all()
        profesores = Profesor.objects.all()
        periodos = PeriodoCELE.objects.filter(activo=True)
        
        if usuario.is_superuser == 1:
            status = 'admin'

        for grupo in grupos:
            if grupo.name == 'Administradores CELE':
                status = 'admin'
            else:
                status = 'null'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        context['cursos'] = cursos
        context['profesores'] = profesores
        context['periodos'] = periodos

        return context
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(RegistroCeleListView, self).get(*args, **kwargs)

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
        usuario_log = usuario

        cursos = CursoCELE.objects.all()
        profesores = Profesor.objects.all()
        periodos = PeriodoCELE.objects.filter(activo=True)

        if usuario.is_superuser == 1:
            status = 'admin'

        for grupo in grupos:
            if grupo.name == 'Administradores CELE':
                status = 'admin'
            else:
                status = 'null'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        context['cursos'] = cursos
        context['profesores'] = profesores
        context['periodos'] = periodos
        return context
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores CELE":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchRegistroCeleView, self).get(*args, **kwargs)



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
        usuario_log = usuario

        cursos = CursoEDCON.objects.all()
        profesores = Instructor.objects.all()
        periodos = PeriodoEDCON.objects.filter(activo=True)

        if usuario.is_superuser == 1:
            status = 'admin'

        for grupo in grupos:
            if grupo.name == 'Administradores EDCON':
                status = 'admin'
            else:
                status = 'null'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        context['cursos'] = cursos
        context['profesores'] = profesores
        context['periodos'] = periodos
        return context
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(RegistroEdconListView, self).get(*args, **kwargs)

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
        usuario_log = usuario

        cursos = CursoEDCON.objects.all()
        profesores = Instructor.objects.all()
        periodos = PeriodoEDCON.objects.filter(activo=True)

        if usuario.is_superuser == 1:
            status = 'admin'

        for grupo in grupos:
            if grupo.name == 'Administradores EDCON':
                status = 'admin'
            else:
                status = 'null'
        
        context['status'] = status
        context['usuario_log'] = usuario_log
        context['cursos'] = cursos
        context['profesores'] = profesores
        context['periodos'] = periodos
        return context
    
    def get(self, *args, **kwargs):
        grupos = self.request.user.groups.all()
        for grupo in grupos:
            if grupo.name != "Administradores EDCON":
                return redirect('/no_autorizado')
        if not self.request.user.is_authenticated:
            return redirect('/login')
        return super(SearchRegistroEdconView, self).get(*args, **kwargs)