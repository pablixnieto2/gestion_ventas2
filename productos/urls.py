from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.producto_create, name='producto_create'),
    path('listar/', views.producto_list, name='producto_list'),
    path('<int:id>/', views.producto_detail, name='producto_detail'),
    path('<int:id>/editar/', views.producto_edit, name='producto_edit'),
    path('<int:id>/eliminar/', views.producto_delete, name='producto_delete'),
]
