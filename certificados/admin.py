from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Empresa,
    Documento,
    DocumentoLogo,
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

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Documento, DocumentoAdmin)
