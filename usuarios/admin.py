from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Usuario
from .forms import (
    # UserChangeForm, 
    UserCreationForm, 
    CustomAdminAuthenticationForm,
)


@admin.register(Usuario)
class UserAdmin(DjangoUserAdmin):
    # form = UserChangeForm
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

admin.site.login_form = CustomAdminAuthenticationForm