from django.contrib import admin
from .models import Pedido, PedidoProducto

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoProductoInline]

admin.site.register(Pedido, PedidoAdmin)
