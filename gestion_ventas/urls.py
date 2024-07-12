from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('clientes/', include('clientes.urls')),
    path('pagos/', include('pagos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('productos/', include('productos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
    path('ventas/', include('ventas.urls')),
]
