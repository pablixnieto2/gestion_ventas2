from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('<str:id>/', views.pedido_detail, name='pedido_detail'),
    path('nuevo/', views.pedido_create, name='pedido_create'),
    path('editar/<str:id>/', views.pedido_update, name='pedido_update'),
    path('eliminar/<str:id>/', views.pedido_delete, name='pedido_delete'),
]
