from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.usuario_create, name='usuario_create'),
    path('listar/', views.usuario_list, name='usuario_list'),
    path('<int:id>/', views.usuario_detail, name='usuario_detail'),
    path('<int:id>/editar/', views.usuario_edit, name='usuario_edit'),
    path('<int:id>/eliminar/', views.usuario_delete, name='usuario_delete'),
]
