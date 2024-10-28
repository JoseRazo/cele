from django.contrib import admin, messages
from django.db.models import Q
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin, ExportMixin
from django.contrib.auth.hashers import make_password
from .models import Curso, Periodo, Instructor, Estudiante, CursoEstudiante
from .forms import (
    EstudianteChangeForm,
    EstudianteCreationForm,
    InstructorCreationForm,
    PeriodoCreationForm,
)
from gestion_escolar.forms import (
    # ProfesorChangeForm,
    ProfesorCreationForm,
)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_curso', 'precio_estudiante_uts', 'precio_persona_externa', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    prepopulated_fields = {'slug': ('nombre',)}


class PeriodoAdmin(admin.ModelAdmin):
    form = PeriodoCreationForm
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class CursoEstudianteResource(resources.ModelResource):
    class Meta:
        model = CursoEstudiante
        fields = ('estudiante__nombre', 'estudiante__apellido_paterno', 'curso__nombre', 'instructor__nombre', 'periodo__nombre',)
        export_order = ('estudiante__nombre', 'estudiante__apellido_paterno', 'curso__nombre', 'instructor__nombre', 'periodo__nombre',)

class CursoEstudianteAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CursoEstudianteResource
    list_display = ('estudiante', 'curso', 'instructor',
                    'periodo', 'inscrito', 'estatus', 'fecha_creacion',)
    list_filter = ('curso',)
    search_fields = ('estudiante__nombre', 'estudiante__username', 'estudiante__email', 'curso__nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Administradores EDCON'):
            return qs
        elif request.user.groups.filter(name='Estudiantes EDCON'):
            return qs.filter(Q(estudiante=request.user, inscrito=True))
        return qs.filter(Q(instructor=request.user, inscrito=True))

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        if obj:
            if request.user.groups.filter(name='Instructores EDCON'):
                form.base_fields["estudiante"].disabled = True
                form.base_fields["curso"].disabled = True
                form.base_fields["instructor"].disabled = True
                form.base_fields["periodo"].disabled = True
                form.base_fields["inscrito"].disabled = True
            return form
        return form


class CursoEstudianteInline(admin.TabularInline):
    model = CursoEstudiante
    extra = 0

class EstudianteResource(resources.ModelResource):
    tipo_usuario = fields.Field(column_name='tipo_usuario')
    genero = fields.Field(column_name='genero')
    carrera = fields.Field(column_name='carrera')

    def dehydrate_tipo_usuario(self, estudiante):
        return estudiante.get_tipo_usuario_display()

    def dehydrate_genero(self, estudiante):
        return estudiante.get_genero_display()
    
    def dehydrate_carrera(self, estudiante):
        return estudiante.carrera.nombre if estudiante.carrera else ""
    
    def before_import_row(self, row, **kwargs):
        value = str(row['password'])
        row['password'] = make_password(value)

        tipo_usuario_display = {v: k for k, v in Estudiante.ROLE_CHOICES}
        genero_display = {v: k for k, v in Estudiante.GENERO_CHOICES}

        if row.get('tipo_usuario') in tipo_usuario_display:
            row['tipo_usuario'] = tipo_usuario_display[row['tipo_usuario']]

        if row.get('genero') in genero_display:
            row['genero'] = genero_display[row['genero']]

    class Meta:
        model = Estudiante
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', 'usuario_ptr', 'last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_active', 'date_joined', 'avatar', 'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior',)
        export_order = ('username', 'password', 'tipo_usuario', 'genero', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono',)
        import_id_fields = ('username', 'password', 'tipo_usuario', 'genero', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono',)

@admin.register(Estudiante)
class EstudianteAdmin(DjangoUserAdmin, ImportExportModelAdmin):
    resource_class = EstudianteResource
    inlines = [CursoEstudianteInline]
    form = EstudianteChangeForm
    add_form = EstudianteCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'contraseña',)}),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'carrera', 'genero', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
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
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'carrera', 'genero', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
    )

    search_fields = ('username', 'email', 'nombre')
    list_filter = ('tipo_usuario', 'is_active', 'genero')
    # autocomplete_fields = ['estado', 'ciudad', 'colonia']
    # class Media:
    #     js = ("usuarios/newajax.js",)


@admin.register(Instructor)
class InstructorAdmin(DjangoUserAdmin):
    # form = ProfesorChangeForm
    add_form = InstructorCreationForm
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
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(CursoEstudiante, CursoEstudianteAdmin)