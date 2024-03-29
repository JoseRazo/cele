from django.contrib import admin
from django.db.models import Q
from .models import ReferenciasBanco, ReferenciasConceptosBanco, Periodo
from rangefilter.filters import DateRangeFilter
from import_export import resources
from import_export.admin import ExportMixin

class ReferenciasBancoResource(resources.ModelResource):
    class Meta:
        model = ReferenciasBanco
        fields = (
            'cve_referencia', 'concepto', 'matricula', 'accion', 'referencia', 'banco_emisor',
            'servicio_bb', 'monto', 'forma_pago', 'monto_parcial_minimo', 'firma', 'estatus',
            'mensaje', 'monto_original', 'recargo_aplicado', 'descuento_aplicado',
            'monto_a_pagar', 'nombre', 'no_recibo', 'folio_pago', 'fecha_limite_pago',
            'fecha_pago', 'hora_pago', 'folio_reverso', 'fecha_reverso', 'hora_reverso',
            'cve_periodo', 'fecha_creacion', 'fecha_actualizacion',
        )

class PeriodoFilter(admin.SimpleListFilter):
    title = 'Periodo'  # Título del filtro
    parameter_name = 'periodo'  # Nombre del parámetro GET

    def lookups(self, request, model_admin):
        # Genera las opciones del filtro a partir de los periodos únicos
        return model_admin.get_unique_periodos(model_admin)

    def queryset(self, request, queryset):
        # Filtra los registros según el periodo seleccionado
        if self.value():
            return queryset.filter(cve_periodo=self.value())
        
class ReferenciasBancoAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ReferenciasBancoResource
    list_display = ('referencia', 'concepto','nombre', 'matricula', 'mensaje', 'forma_pago', 'fecha_pago')
    search_fields = ('referencia', 'matricula', 'concepto', 'nombre',)

    def get_unique_periodos(self, model_admin):
        periodos = model_admin.model.objects.values_list('cve_periodo', flat=True).distinct()
        unique_periodos = Periodo.objects.filter(cve_periodo__in=periodos).order_by('-fecha_inicio')  # Ordenar por fecha_inicio de forma descendente
        periodos_choices = [(periodo.cve_periodo, f"{periodo.fecha_inicio.strftime('%B')} - {periodo.fecha_fin.strftime('%B')} {periodo.fecha_inicio.year}") for periodo in unique_periodos]
        return periodos_choices
    
    list_filter = (
        'mensaje', 
        'concepto', 
        'monto',
        PeriodoFilter,
        ('fecha_pago', DateRangeFilter),
    )
    
    list_per_page = 20

    def has_add_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Administradores CELE'):
            return qs.filter(Q(servicio_bb='2354'))
        elif request.user.groups.filter(name='Administradores EDCON'):
            return qs.filter(Q(servicio_bb='2355'))
        return qs.filter(Q(servicio_bb='2354') | Q(servicio_bb='2355') | Q(servicio_bb='2123'))
    
class ReferenciasConceptosBancoAdmin(admin.ModelAdmin):
    # Ordena los campos en el formulario
    fields = ['num_concepto', 'concepto', 'monto', 'monto_externo', 'preferencial', 'monto_preferencial', 'fecha_limite', 'fecha_limite_pago', 'activo', 'cve_servicio', 'fecha_creacion', 'fecha_actualizacion']
    list_display = ('concepto', 'monto', 'monto_externo', 'preferencial', 'monto_preferencial', 'fecha_limite', 'fecha_limite_pago', 'activo',)
    readonly_fields = ['num_concepto', 'concepto', 'cve_servicio', 'fecha_creacion', 'fecha_actualizacion']
    list_filter = ('activo',)
    search_fields = ('concepto',)

    # def has_add_permission(self, request, obj=None):
    #         return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Administradores CELE'):
            return qs.filter(Q(cve_servicio='2'))
        elif request.user.groups.filter(name='Administradores EDCON'):
            return qs.filter(Q(cve_servicio='3'))
        return qs.filter(Q(cve_servicio='2') | Q(cve_servicio='3'))



admin.site.register(ReferenciasBanco, ReferenciasBancoAdmin)
admin.site.register(ReferenciasConceptosBanco, ReferenciasConceptosBancoAdmin)
