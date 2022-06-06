from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Usuario, Alumno, Profesor
from .forms import (
    UserChangeForm, 
    UserCreationForm, 
    CustomAdminAuthenticationForm, 
    AlumnoChangeForm, AlumnoCreationForm, 
    ProfesorChangeForm, 
    ProfesorCreationForm
)


@admin.register(Usuario)
class UserAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email')}),
        # (_('Domicilio Actual'), {'fields': (
        #     'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'is_staff'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email')}),
        # (_('Domicilio Actual'), {'fields': (
        #     'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')

@admin.register(Alumno)
class AlumnoAdmin(DjangoUserAdmin):
    form = AlumnoChangeForm
    add_form = AlumnoCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'tipo_usuario', 'inscrito', 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'inscrito', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('tipo_usuario', 'inscrito', 'is_active')

@admin.register(Profesor)
class ProfesorAdmin(DjangoUserAdmin):
    form = ProfesorChangeForm
    add_form = ProfesorCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'telefono', 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('is_active', 'is_staff')

admin.site.login_form = CustomAdminAuthenticationForm