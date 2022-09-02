from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.hashers import make_password
from .models import Alumno, CalificacionCurso, Profesor, Curso, Periodo, Grupo, Aula, CursoAlumno
from .forms import (
    GrupoCreationForm,
    AlumnoChangeForm, 
    AlumnoCreationForm,
    ProfesorChangeForm,
    ProfesorCreationForm,
)

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_estudiante_uts', 'precio_persona_externa', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class GrupoAdmin(admin.ModelAdmin):
    form = GrupoCreationForm
    filter_horizontal = ('alumnos',)
    list_display = ('nombre', 'periodo', 'codigo', 'profesor', 'aula', 'fecha_creacion',)
    search_fields = ('nombre', 'codigo', 'profesor__nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)
    list_filter = ('curso', 'aula', 'profesor',)
    # autocomplete_fields = ['profesor', 'aula']
    # class Media:
    #     js = ("gestion_escolar/newajax.js",)

class AulaAdmin(admin.ModelAdmin):
    list_display = ('edificio', 'num_aula', 'fecha_creacion',)
    list_filter = ('edificio',)
    search_fields = ('edificio', 'num_aula',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

class CalificacionCursoInline(admin.TabularInline):
    model = CalificacionCurso
    extra = 0

class CursoAlumnoAdmin(admin.ModelAdmin):
    inlines = [CalificacionCursoInline]
    list_display = ('alumno', 'curso', 'periodo', 'fecha_creacion',)
    list_filter = ('curso',)
    search_fields = ('alumno__nombre', 'curso__nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

class CursoAlumnoInline(admin.TabularInline):
    model = CursoAlumno
    extra = 0

class AlumnoResource(resources.ModelResource):
    # fields = ('id', 'username', 'password', 'tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')
    def before_import_row(self, row, **kwargs):
            value = str(row['password'])
            row['password'] = make_password(value)
    class Meta:
        model = Alumno
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', 'usuario_ptr', 'last_login', 'is_superuser', 'user_permissions', 'is_active', 'date_joined', 'avatar',)
        export_order = ('username', 'password', 'is_staff', 'groups', 'tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior',)
        import_id_fields = ('username', 'password', 'is_staff', 'groups', 'tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior',)

@admin.register(Alumno)
class AlumnoAdmin(DjangoUserAdmin, ImportExportModelAdmin):
    resource_class = AlumnoResource
    inlines = [CursoAlumnoInline]
    form = AlumnoChangeForm
    add_form = AlumnoCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'tipo_usuario', 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('tipo_usuario', 'is_active')
    # autocomplete_fields = ['estado', 'ciudad', 'colonia']
    # class Media:
    #     js = ("usuarios/newajax.js",)

@admin.register(Profesor)
class ProfesorAdmin(DjangoUserAdmin):
    form = ProfesorChangeForm
    add_form = ProfesorCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'telefono', 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('is_active', 'is_staff')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(CursoAlumno, CursoAlumnoAdmin)