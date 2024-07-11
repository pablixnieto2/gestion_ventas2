from django.urls import path
from . import views

urlpatterns = [
    path('venta/', views.lista_productos_venta, name='lista_productos_venta'),
    path('venta/<int:pk>/', views.detalle_producto_venta, name='detalle_producto_venta'),
    path('venta/nuevo/', views.crear_producto_venta, name='crear_producto_venta'),
    path('venta/editar/<int:pk>/', views.editar_producto_venta, name='editar_producto_venta'),
    path('venta/eliminar/<int:pk>/', views.eliminar_producto_venta, name='eliminar_producto_venta'),
    path('alquiler/', views.lista_productos_alquiler, name='lista_productos_alquiler'),
    path('alquiler/<int:pk>/', views.detalle_producto_alquiler, name='detalle_producto_alquiler'),
    path('alquiler/nuevo/', views.crear_producto_alquiler, name='crear_producto_alquiler'),
    path('alquiler/editar/<int:pk>/', views.editar_producto_alquiler, name='editar_producto_alquiler'),
    path('alquiler/eliminar/<int:pk>/', views.eliminar_producto_alquiler, name='eliminar_producto_alquiler'),
]
