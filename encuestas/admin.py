from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import (
    Encuesta,
    Seccion,
    TipoPregunta,
    Pregunta,
    EncuestaAlumno,
    EncuestaEstudiante,
    RegistrosCELE,
    RegistrosEDCON
    # Opcion,
    # Respuesta
)

# Register your models here.

class EncuestaAdmin(admin.ModelAdmin):
    # inlines = [PreguntaInline]
    list_display = ('nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')

# class OpcionInline(admin.StackedInline):
#     model = Opcion
#     extra = 1

class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_actualizacion')

class PreguntaAdmin(admin.ModelAdmin):
    # inlines = [OpcionInline]
    list_display = ('texto_pregunta', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('encuesta',)

class TipoPreguntaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_actualizacion')

class OpcionAdmin(admin.ModelAdmin):
    list_display = ('texto_opcion', 'valor', 'fecha_creacion', 'fecha_actualizacion')

class EncuestaAlumnoInline(admin.StackedInline):
    model = EncuestaAlumno
    fields = ['pregunta', 'texto_respuesta']
    readonly_fields = ('pregunta', 'texto_respuesta')
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

class EncuestaEstudianteInline(admin.StackedInline):
    model = EncuestaEstudiante
    fields = ['pregunta', 'texto_respuesta']
    readonly_fields = ('pregunta', 'texto_respuesta')
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

class RegistrosCELEAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('usuario', 'curso_alumno', 'encuesta', 'fecha_creacion', 'fecha_actualizacion')
    inlines = [EncuestaAlumnoInline]

class RegistrosEDCONAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('usuario', 'curso_alumno', 'encuesta', 'fecha_creacion', 'fecha_actualizacion')
    inlines = [EncuestaEstudianteInline]

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(TipoPregunta, TipoPreguntaAdmin)
admin.site.register(RegistrosCELE, RegistrosCELEAdmin)
admin.site.register(RegistrosEDCON, RegistrosEDCONAdmin)