from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('<str:id>/', views.producto_detail, name='producto_detail'),
    path('nuevo/', views.producto_create, name='producto_create'),
    path('editar/<str:id>/', views.producto_update, name='producto_update'),
    path('eliminar/<str:id>/', views.producto_delete, name='producto_delete'),
]
