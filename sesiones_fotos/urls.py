from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.sesion_foto_create, name='sesion_foto_create'),
    path('listar/', views.sesion_foto_list, name='sesion_foto_list'),
    path('<int:id>/', views.sesion_foto_detail, name='sesion_foto_detail'),
    path('<int:id>/editar/', views.sesion_foto_edit, name='sesion_foto_edit'),
    path('<int:id>/eliminar/', views.sesion_foto_delete, name='sesion_foto_delete'),
]
