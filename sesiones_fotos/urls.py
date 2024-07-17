from django.urls import path
from . import views

app_name = 'sesiones_fotos'  # Definir el namespace

urlpatterns = [
    path('', views.SesionFotoListView.as_view(), name='sesionfoto-list'),
    path('<int:pk>/', views.SesionFotoDetailView.as_view(), name='sesionfoto-detail'),
    path('create/', views.SesionFotoCreateView.as_view(), name='sesionfoto-create'),
    path('<int:pk>/update/', views.SesionFotoUpdateView.as_view(), name='sesionfoto-update'),
    path('<int:pk>/delete/', views.SesionFotoDeleteView.as_view(), name='sesionfoto-delete'),
]
