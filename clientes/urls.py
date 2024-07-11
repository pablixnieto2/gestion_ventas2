from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
]
