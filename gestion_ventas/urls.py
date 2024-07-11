from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def test_view(request):
    return HttpResponse('La configuración de plantillas está funcionando')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('ventas/', include('ventas.urls')),
    path('pagos/', include('pagos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('test/', test_view),  # Asegúrate de incluir esta línea para la vista de prueba
]
