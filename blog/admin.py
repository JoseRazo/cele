from django.contrib import admin

# Register your models here.

from .models import Slider, CategoriaSlider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'activo', 'fecha_creacion')

@admin.register(CategoriaSlider)
class CategoriaSliderAdmin(admin.ModelAdmin):
    list_display = ('nombre',)