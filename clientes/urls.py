from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.cliente_create, name='cliente_create'),
    path('listar/', views.cliente_list, name='cliente_list'),
    path('<int:id>/', views.cliente_detail, name='cliente_detail'),
    path('<int:id>/editar/', views.cliente_edit, name='cliente_edit'),
    path('<int:id>/eliminar/', views.cliente_delete, name='cliente_delete'),
]
