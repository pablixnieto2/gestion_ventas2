from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('<int:pk>/', views.detalle_venta, name='detalle_venta'),
    path('nueva/', views.crear_venta, name='crear_venta'),
    path('editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
]
