from django.contrib import admin
from django.urls import path, include
from django_select2 import urls as select2_urls
from gestion_ventas2.views import home  # Asegúrate de que la vista home esté correctamente importada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('productos/', include('productos.urls', namespace='productos')),
    path('ventas/', include('ventas.urls', namespace='ventas')),
    path('pagos/', include('pagos.urls', namespace='pagos')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
    path('sesiones_fotos/', include('sesiones_fotos.urls', namespace='sesiones_fotos')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('select2/', include(select2_urls)),  # Incluye esta línea
]
