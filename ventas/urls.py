from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.venta_create, name='venta_create'),
    path('listar/', views.venta_list, name='venta_list'),
    path('<int:id>/', views.venta_detail, name='venta_detail'),
    path('<int:id>/editar/', views.venta_edit, name='venta_edit'),
    path('<int:id>/eliminar/', views.venta_delete, name='venta_delete'),
]
