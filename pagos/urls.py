from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.pago_list, name='pago_list'),
    path('<str:id>/', views.pago_detail, name='pago_detail'),
    path('nuevo/', views.pago_create, name='pago_create'),
    path('editar/<str:id>/', views.pago_update, name='pago_update'),
    path('eliminar/<str:id>/', views.pago_delete, name='pago_delete'),
]
