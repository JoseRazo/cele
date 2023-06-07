from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm
from edcon.models import CursoEstudiante, Estudiante
from edcon.models import Curso as Curso2
from gestion_escolar.models import Alumno, CursoAlumno, Periodo, CalificacionCurso, Curso
from usuarios.models import Usuario
from datetime import date as fecha_actual

import io
from pathlib import Path
import os
from .forms import ProfileForm
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from .models import CertificadoAlumno, Plantilla
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('certificados:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
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
                error_message = "Por favor introduzca un nombre de usuario y contraseña correctos."
                messages.error(request, error_message)
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

    # if request.user.is_authenticated:
    #     return redirect('certificados:dashboard')
    # form = LoginForm(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     usuario = authenticate(request, username=username, password=password)
    #     if usuario is not None:
    #         auth_login(request, usuario)
    #         if 'next' in request.GET:
    #             return redirect(request.GET['next'])
    #         return redirect("certificados:dashboard")
    #     else:
    #         error_message = "Por favor introduzca un nombre de usuario y contraseña correctos."
    #         context = {
    #             'form': form,
    #             'error_message': error_message
    #         }
    #         return render(request, 'registration/login.html', context)
    # context = {
    #     'form': form,
    # }
    # return render(request, 'registration/login.html', context)

def logout_view(request):
    auth_logout(request)
    # Redirigir a la página de inicio o cualquier otra página deseada después del logout
    return redirect('certificados:login')

def profile_user(request):
   
    usuario = request.user

    if usuario.is_staff == 1:
        alumno = Usuario.objects.get(username=usuario.username)
    else:
        filtro = str(Alumno.objects.filter(username=usuario.username))
        if filtro == "<QuerySet []>":
            alumno = Estudiante.objects.get(username=usuario.username)
        else:
            alumno = Alumno.objects.get(username=usuario.username)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('certificados:profile')  # Redirige a la página de perfil actualizada
    else:
        form = ProfileForm(instance=alumno)

    return render(request, "certificados/profile.html", {'form': form, 'alumno': alumno, 'usuario': usuario})

def curso_info(request):
    usuario = request.user
    filtro = str(Alumno.objects.filter(username=usuario.username))
    
    if filtro == "<QuerySet []>":
        alumno = Estudiante.objects.get(username=usuario.username)
    else:
        alumno = Alumno.objects.get(username=usuario.username)
    
    grupos = request.user.groups.all()
    curso_list = []
    calificacion_curso = None
    estatus_curso = None
        
    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            curso_list = CursoAlumno.objects.filter(alumno=usuario)
            if curso_list:
                try:
                    curso_alumno = curso_list[0]
                    calificacion_curso = CalificacionCurso.objects.get(curso_alumno=curso_alumno)
                except ObjectDoesNotExist:
                    pass
        elif grupo.name == 'Estudiantes EDCON':
            curso_list = CursoEstudiante.objects.filter(estudiante=usuario)

    return render(request, "certificados/info.html", {'curso_list': curso_list, 'calificacion_curso': calificacion_curso, 'alumno': alumno})


def Cursos_det(request, curso_id):
    usuario = request.user
    curso_periodo = []
    curso_data = []
    grupos = request.user.groups.all()
    curso_list = []
    today = fecha_actual.today()

    filtro = str(Alumno.objects.filter(username=usuario.username))
    if filtro == "<QuerySet []>":
        curso_list = CursoEstudiante.objects.get(pk=curso_id)
        alumno = Estudiante.objects.get(username=usuario.username)
    else:
        curso_list = CursoAlumno.objects.get(pk=curso_id)
        alumno = Alumno.objects.get(username=usuario.username)

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            curso_list = CursoAlumno.objects.get(pk=curso_id)
            curso_data = Curso.objects.all()
            curso_periodo = Curso.objects.all()
        elif grupo.name == 'Estudiantes EDCON':
            curso_data = Curso2.objects.all()
            curso_periodo = Curso.objects.all()
            curso_list = CursoEstudiante.objects.get(pk=curso_id)    

    return render(request, 'certificados/cursos_detail.html', {'curso_list': curso_list, 'alumno': alumno, 'today': today, 'curso_data': curso_data, 'curso_periodo': curso_periodo})


@login_required
def dash_view(request):
    today = fecha_actual.today()
    usuario = request.user
    curso_data = []
    grupos = request.user.groups.all()
    curso_list = []
    print(curso_data)

    filtro = str(Alumno.objects.filter(username=usuario.username))
    if usuario.is_staff == 1:
        alumno = Alumno.objects.filter(username=usuario.username)
    elif filtro == "<QuerySet []>":
        alumno = Estudiante.objects.get(username=usuario.username)
    elif "Alumno" in filtro:
        alumno = Alumno.objects.get(username=usuario.username)

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            curso_list = CursoAlumno.objects.filter(alumno=usuario, periodo__fecha_fin__gte=today)
            curso_data = Curso.objects.all()
        elif grupo.name == 'Estudiantes EDCON':
            curso_data = Curso2.objects.all()
            curso_list = CursoEstudiante.objects.filter(estudiante=usuario, periodo__fecha_fin__gte=today)

    return render(request, 'certificados/dashboard.html', {'curso_list': curso_list, 'alumno': alumno, 'curso_data': curso_data, 'today': today})