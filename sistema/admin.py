from django.contrib import admin
from .models import Pais, Estado, Ciudad, Colonia
# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'abreviatura')
    search_fields = ('nombre',)
    ordering = ('nombre', 'nacionalidad', 'abreviatura')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviatura', 'pais')
    list_filter = ('pais',)
    search_fields = ('nombre',)
    ordering = ('nombre', 'abreviatura', 'pais')

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lada', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)
    ordering = ('nombre', 'lada', 'estado')

class ColoniaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_postal', 'ciudad')
    list_filter = ('ciudad',)
    search_fields = ('nombre',)
    ordering = ('nombre', 'codigo_postal', 'ciudad')

admin.site.register(Pais, PaisAdmin,)
admin.site.register(Estado, EstadoAdmin,)
admin.site.register(Ciudad, CiudadAdmin,)
admin.site.register(Colonia, ColoniaAdmin,)