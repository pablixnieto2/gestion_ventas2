from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('pagos/', include('pagos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('productos/', include('productos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ventas/', include('ventas.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]
