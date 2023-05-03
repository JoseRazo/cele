from django.contrib import admin
from .models import (
    Empresa,
    Certificado,
)

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'logo',)
    search_fields = ('nombre',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Certificado, CertificadoAdmin)
