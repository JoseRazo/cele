from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm
from gestion_escolar.models import Alumno, CursoAlumno, Periodo
from usuarios.models import Usuario
import io
from pathlib import Path
import os
from .forms import ProfileForm



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
    usuario = request.user
    alumno = Alumno.objects.get(username=usuario.username)

    print(alumno.nombre)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('certificados:profile')  # Redirige a la página de perfil actualizada
    else:
        form = ProfileForm(instance=alumno)

    return render(request, "certificados/profile.html", {'form': form, 'alumno': alumno})

def curso_info(request):
    usuario = request.user
    curso_list = CursoAlumno.objects.filter(alumno=usuario) 
    return render(request, "certificados/info.html", {'curso_list': curso_list})


@login_required
def dash_view(request):
    usuario = request.user
    curso_list = CursoAlumno.objects.filter(alumno=usuario)
   
    return render(request,"certificados/dashboard.html", {'curso_list': curso_list})








  

 



  














