from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('ventas/', include('ventas.urls')),
    path('pagos/', include('pagos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Añade esta línea
]
