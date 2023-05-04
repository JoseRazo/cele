from django.contrib import admin
from .models import (
    Empresa,
    Documento,
    Certificado,
    Logo,
)

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'logo', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('tipo',)

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'titulo', 'tipo', 'firma', 'sello', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

class LogoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(Logo, LogoAdmin)
