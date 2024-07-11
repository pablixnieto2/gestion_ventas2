from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pagos, name='lista_pagos'),
    path('<int:pk>/', views.detalle_pago, name='detalle_pago'),
    path('nuevo/', views.crear_pago, name='crear_pago'),
    path('editar/<int:pk>/', views.editar_pago, name='editar_pago'),
    path('eliminar/<int:pk>/', views.eliminar_pago, name='eliminar_pago'),
]
