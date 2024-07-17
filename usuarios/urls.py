from django.urls import path
from . import views

app_name = 'usuarios'  # Definir el namespace

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='usuario-list'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('create/', views.UsuarioCreateView.as_view(), name='usuario-create'),
    path('<int:pk>/update/', views.UsuarioUpdateView.as_view(), name='usuario-update'),
    path('<int:pk>/delete/', views.UsuarioDeleteView.as_view(), name='usuario-delete'),
]
