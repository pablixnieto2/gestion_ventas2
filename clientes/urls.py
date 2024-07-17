from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('<str:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('<str:pk>/update/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('<str:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
