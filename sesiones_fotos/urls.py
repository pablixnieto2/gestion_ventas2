from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_sesiones_fotos, name='lista_sesiones_fotos'),
    path('<int:pk>/', views.detalle_sesion_fotos, name='detalle_sesion_fotos'),
    path('nueva/', views.crear_sesion_fotos, name='crear_sesion_fotos'),
    path('editar/<int:pk>/', views.editar_sesion_fotos, name='editar_sesion_fotos'),
    path('eliminar/<int:pk>/', views.eliminar_sesion_fotos, name='eliminar_sesion_fotos'),
]
