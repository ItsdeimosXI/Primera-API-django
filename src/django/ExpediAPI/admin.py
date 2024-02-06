from django.contrib import admin
from .models import expedientes, Proveedor
# Register your models here.


class expedientesAdmin(admin.ModelAdmin):
    list_display=(
        'nro_pago',
        'nro_expediente',
        'detalles',
        'año',
        'valor'   
    )
admin.site.register(Proveedor)
admin.site.register(expedientes, expedientesAdmin)
