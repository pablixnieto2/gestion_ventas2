from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('nuevo/', views.crear_pedido, name='crear_pedido'),
    path('editar/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
]
