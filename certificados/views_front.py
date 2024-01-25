from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm
from edcon.models import CursoEstudiante, Estudiante, Instructor
from edcon.models import Curso as Curso2
from gestion_escolar.models import Alumno, CursoAlumno, Periodo, CalificacionCurso, Curso, Profesor
from usuarios.models import Usuario
from datetime import date as fecha_actual
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

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

@login_required
def profile_user(request):
    usuario = request.user
    user_perfil = Usuario.objects.get(username=usuario.username)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_perfil)
        if form.is_valid():
            if request.FILES.get('avatar'):
                avatar = request.FILES['avatar']

                # Verificar las dimensiones de la imagen
                width, height = get_image_dimensions(avatar)
                if width > 512 or height > 512:
                    messages.error(request, 'Las dimensiones de la imagen no deben ser mayores de 512 píxeles.')
                    return redirect('certificados:profile')
                if request.user.avatar and request.user.avatar.name.endswith('default.png'):
                    # Si el avatar es default.png, conservar la imagen predeterminada.
                    form.save()
                    messages.success(request, '¡Tu perfil ha sido actualizado!')
                else:
                    # Si el avatar es diferente a default.png, eliminar la imagen actual.
                    request.user.avatar.delete()
                    form.save()
                    messages.success(request, '¡Tu perfil ha sido actualizado!')
            else:
                # Conservar la imagen actual en caso de no haber seleccionado otra.
                user_perfil.avatar = user_perfil.avatar
                user_perfil.save()
                messages.warning(request, 'No seleccionaste una nueva imagen. Tu perfil no ha sido actualizado.')
            return redirect("certificados:profile")
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ProfileForm(instance=user_perfil)
    return render(request, 'certificados/profile.html', {'form': form})

@login_required
def dash_view(request):
    today = fecha_actual.today()
    usuario = request.user
    status = ''
    grupos = request.user.groups.all()
    curso_list = []

    if 'CELE' or 'EDCON' not in str(grupos) and usuario.is_superuser == 0:
        usuario_log = request.user

    for grupo in grupos:
        if grupo.name == 'Alumnos CELE':
            curso_list = CursoAlumno.objects.filter(alumno=usuario, periodo__fecha_fin__gte=today, inscrito=True)
            usuario_log = Alumno.objects.get(username=usuario.username)
            status = 'alumno'
        elif grupo.name == 'Estudiantes EDCON':
            curso_list = CursoEstudiante.objects.filter(estudiante=usuario, estatus=1, inscrito=True)
            usuario_log = Estudiante.objects.get(username=usuario.username)
            status = 'estudiante'
        elif grupo.name == 'Profesores CELE':
            usuario_log = Profesor.objects.get(username=usuario.username)
            status = 'profe'
        elif grupo.name == 'Instructores EDCON':
            usuario_log = Instructor.objects.get(username=usuario.username)
            status = 'instru'
        elif grupo.name in ['Administradores CELE', 'Administradores EDCON', 'Admin Constancias'] or usuario.is_superuser:
            usuario_log = request.user
            status = 'admin'

    return render(request, 'certificados/dashboard.html', {'curso_list': curso_list, 'usuario_log': usuario_log, 'today': today, 'status': status})