from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Alumno
from .forms import AlumnoChangeForm, AlumnoCreationForm


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
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'tipo_usuario', 'date_joined'
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
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

