from django.contrib import admin, messages
from .models import Curso, Nivel, Grupo, Aula
from .forms import GrupoCreationForm

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_estudiante_uts', 'precio_persona_externa', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class NivelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

# class InscribirAlumnoAdmin(admin.ModelAdmin):
#     list_display = ('alumno', 'curso', 'nivel', 'inscrito')
#     list_filter = ('inscrito', 'curso', 'nivel')
#     search_fields = ('alumno__nombre',)
#     readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)
    # def response_add(self, request, obj, post_url_continue=None):
    #     msg =  'El alumno %s ha sido inscrito en el curso %s %s' % (obj.alumno, obj.curso, obj.nivel)
    #     self.message_user(request, msg, level=messages.SUCCESS)
    #     return self.response_post_save_add(request, obj)
    # def response_change(self, request, obj):
    #     msg =  'El estatus del alumno %s se cambió correctamente.' % (obj.alumno)
    #     self.message_user(request, msg, level=messages.SUCCESS)
    #     return self.response_post_save_change(request, obj)

class GrupoAdmin(admin.ModelAdmin):
    form = GrupoCreationForm
    filter_horizontal = ('alumnos',)
    list_display = ('nombre', 'codigo', 'profesor', 'aula', 'fecha_creacion',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)
    # prepopulated_fields = {'slug': ('nombre',)}

class AulaAdmin(admin.ModelAdmin):
    list_display = ('edificio', 'num_aula', 'fecha_creacion',)
    list_filter = ('edificio',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Nivel, NivelAdmin)
# admin.site.register(InscribirAlumno, InscribirAlumnoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Aula, AulaAdmin)