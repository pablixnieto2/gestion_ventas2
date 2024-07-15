from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.pedido_create, name='pedido_create'),
    path('listar/', views.pedido_list, name='pedido_list'),
    path('<int:id>/', views.pedido_detail, name='pedido_detail'),
    path('<int:id>/editar/', views.pedido_edit, name='pedido_edit'),
    path('<int:id>/eliminar/', views.pedido_delete, name='pedido_delete'),
]
