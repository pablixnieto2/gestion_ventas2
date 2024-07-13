from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesionfoto_list, name='sesionfoto_list'),
    path('<str:id>/', views.sesionfoto_detail, name='sesionfoto_detail'),
    path('nueva/', views.sesionfoto_create, name='sesionfoto_create'),
    path('editar/<str:id>/', views.sesionfoto_update, name='sesionfoto_update'),
    path('eliminar/<str:id>/', views.sesionfoto_delete, name='sesionfoto_delete'),
]
