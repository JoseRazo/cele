from django.contrib import admin
from django.db.models import Q

# Register your models here.

from .models import ReferenciasBanco

class ReferenciasBancoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'concepto','nombre', 'matricula', 'mensaje',)
    list_filter = ('mensaje',)
    search_fields = ('referencia', 'matricula', 'concepto', 'nombre',)
    # fields = ('nombre', 'matricula', 'concepto', 'referencia', 'banco_emisor', 'servicio_bb')
    list_per_page = 20

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Administradores CELE'):
            return qs.filter(Q(servicio_bb='2354 - UTS CELE'))
        elif request.user.groups.filter(name='Administradores EDCON'):
            return qs.filter(Q(servicio_bb='2355 - UTS SERVICIOS'))
        return qs
    




admin.site.register(ReferenciasBanco, ReferenciasBancoAdmin)
