from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.hashers import make_password
from .models import Curso
from gestion_escolar.models import Profesor
from gestion_escolar.forms import (
    ProfesorChangeForm,
    ProfesorCreationForm,
)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_estudiante_uts', 'precio_persona_externa', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

# @admin.register(Profesor)
# class ProfesorAdmin(DjangoUserAdmin):
#     form = ProfesorChangeForm
#     add_form = ProfesorCreationForm
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
#          'apellido_materno', 'email', 'telefono', 'avatar')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'groups'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )

#     list_display = (
#         'username', 'email', 'nombre', 'telefono', 'date_joined'
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#         (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
#          'apellido_materno', 'email', 'telefono', 'avatar')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'groups'),
#         }),
#     )

#     search_fields = ('username', 'email', 'nombre')
#     list_filter = ('is_active', 'is_staff')

admin.site.register(Curso, CursoAdmin)