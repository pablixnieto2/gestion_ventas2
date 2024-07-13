from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_list, name='venta_list'),
    path('<str:id>/', views.venta_detail, name='venta_detail'),
    path('nueva/', views.venta_create, name='venta_create'),
    path('editar/<str:id>/', views.venta_update, name='venta_update'),
    path('eliminar/<str:id>/', views.venta_delete, name='venta_delete'),
]
