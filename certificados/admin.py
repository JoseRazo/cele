from django.contrib import admin
from .models import (
    Empresa,
    Documento,
    Certificado,
    Logo,
)

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'titulo', 'firma', 'sello',)
    search_fields = ('nombre',)

class LogoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen',)
    search_fields = ('nombre',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(Logo, LogoAdmin)
