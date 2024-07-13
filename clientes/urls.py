from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('<str:id>/', views.cliente_detail, name='cliente_detail'),
    path('nuevo/', views.cliente_create, name='cliente_create'),
    path('editar/<str:id>/', views.cliente_update, name='cliente_update'),
    path('eliminar/<str:id>/', views.cliente_delete, name='cliente_delete'),
]
