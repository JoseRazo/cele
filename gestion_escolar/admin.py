from django.contrib import admin, messages
from django.db.models import Q
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from django.contrib.auth.hashers import make_password
from .models import (
    Alumno, 
    CalificacionCurso, 
    Profesor, 
    Curso, 
    Periodo, 
    CursoAlumno, 
    # Grupo, 
    # Aula
)
from .forms import (
    AlumnoChangeForm,
    AlumnoCreationForm,
    # ProfesorChangeForm,
    ProfesorCreationForm,
    CalificacionCursoForm,
    # GrupoCreationForm
)

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_estudiante_uts',
                    'precio_persona_externa', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    prepopulated_fields = {'slug': ('nombre',)}

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

# class CursoAlumnoInline(admin.StackedInline):
#     model = CursoAlumno
#     can_delete = False
#     # fields = ('alumno',)
#     # readonly_fields = ('alumno',)
#     extra = 0

# class GrupoAdmin(admin.ModelAdmin):
#     inlines = [CursoAlumnoInline,]
#     form = GrupoCreationForm
#     filter_horizontal = ('alumnos',)
#     list_display = ('nombre', 'periodo', 'codigo', 'profesor', 'aula', 'fecha_creacion',)
#     search_fields = ('nombre', 'codigo', 'profesor__nombre',)
#     readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)
#     list_filter = ('curso', 'aula', 'profesor',)
#     autocomplete_fields = ['profesor', 'aula']

# class AulaAdmin(admin.ModelAdmin):
#     list_display = ('edificio', 'num_aula', 'fecha_creacion',)
#     list_filter = ('edificio',)
#     search_fields = ('edificio', 'num_aula',)
#     readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

class CursoAlumnoResource(resources.ModelResource):
    class Meta:
        model = CursoAlumno
        fields = ('alumno__nombre', 'alumno__apellido_paterno', 'curso__nombre', 'profesor__nombre', 'periodo__nombre',)
        export_order = ('alumno__nombre', 'alumno__apellido_paterno', 'curso__nombre', 'profesor__nombre', 'periodo__nombre',)

class CalificacionCursoInline(admin.StackedInline):
    form = CalificacionCursoForm
    model = CalificacionCurso
    can_delete = False
    extra = 0


class CursoAlumnoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CursoAlumnoResource
    inlines = [CalificacionCursoInline]
    list_display = ('alumno', 'curso', 'profesor',
                    'periodo', 'inscrito', 'fecha_creacion',)
    list_filter = ('curso',)
    search_fields = ('alumno__nombre', 'alumno__username', 'alumno__email', 'curso__nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Administradores CELE'):
            return qs
        elif request.user.groups.filter(name='Alumnos CELE'):
            return qs.filter(Q(alumno=request.user, inscrito=True))
        return qs.filter(Q(profesor=request.user, inscrito=True))

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        if obj:
            if request.user.groups.filter(name='Profesores CELE'):
                form.base_fields["alumno"].disabled = True
                form.base_fields["curso"].disabled = True
                form.base_fields["profesor"].disabled = True
                form.base_fields["periodo"].disabled = True
                form.base_fields["inscrito"].disabled = True
            return form
        return form

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
        exclude = ('id', 'usuario_ptr', 'last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_active', 'date_joined', 'avatar', 'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior',)
        export_order = ('username', 'password', 'tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono',)
        import_id_fields = ('username', 'password', 'tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono',)


@admin.register(Alumno)
class AlumnoAdmin(DjangoUserAdmin, ImportExportModelAdmin):
    resource_class = AlumnoResource
    inlines = [CursoAlumnoInline]
    form = AlumnoChangeForm
    add_form = AlumnoCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'contraseña',)}),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
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
            'fields': ('username', 'password1', 'password2', 'contraseña',),
        }),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
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
    # form = ProfesorChangeForm
    add_form = ProfesorCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
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
        (_('Datos Generales'), {'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('is_active', 'is_staff')

@admin.register(CalificacionCurso)
class CalificacionCursoAdmin(admin.ModelAdmin):
    list_display = ('curso_alumno', 'primer_examen', 'segundo_examen', 'calificacion_final')
    def has_view_permission(self, request, obj=None):
        if request.user.groups.filter(name='Alumnos CELE'):
            return True
        else:
            return False
    def has_add_permission(self, request, obj=None):
        return False
        
    def has_change_permission(self, request, obj=None):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Alumnos CELE'):
            return qs.filter(Q(curso_alumno__alumno=request.user))
        

admin.site.register(Curso, CursoAdmin)
# admin.site.register(Grupo, GrupoAdmin)
# admin.site.register(Aula, AulaAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(CursoAlumno, CursoAlumnoAdmin)
