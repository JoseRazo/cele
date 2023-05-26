from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Empresa,
    Documento,
    DocumentoLogo,
    CertificadoAlumno,
    CertificadoEstudiante,
    Plantilla
)

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'direccion', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

class DocumentoLogoInline(admin.TabularInline):
    model = DocumentoLogo
    extra = 3

class DocumentoAdmin(admin.ModelAdmin):
    inlines = [DocumentoLogoInline]
    list_display = ('tipo', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('tipo',)

class CertificadoAlumnoAdmin(admin.ModelAdmin):
    list_display = ('curso_alumno', 'get_nombre_alumno', 'plantilla', 'folio', 'firma', 'cadena', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

    def get_nombre_alumno(self, obj):
        return obj.curso_alumno.alumno.nombre_completo()
    get_nombre_alumno.short_description = 'Alumno'

class CertificadoEstudianteAdmin(admin.ModelAdmin):
    list_display = ('curso_alumno', 'get_nombre_alumno', 'plantilla', 'folio', 'firma', 'cadena', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

    def get_nombre_alumno(self, obj):
        return obj.curso_alumno.estudiante.nombre_completo()
    get_nombre_alumno.short_description = 'Estudiante'

class PlantillaAlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'firma_rector', 'fecha_creacion', 'fecha_actualizacion')

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(CertificadoAlumno, CertificadoAlumnoAdmin)
admin.site.register(CertificadoEstudiante, CertificadoEstudianteAdmin)
admin.site.register(Plantilla, PlantillaAlumnoAdmin)