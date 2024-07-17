from django.urls import path
from . import views

app_name = 'pedidos'  # Definir el namespace

urlpatterns = [
    path('', views.PedidoListView.as_view(), name='pedido-list'),
    path('<int:pk>/', views.PedidoDetailView.as_view(), name='pedido-detail'),
    path('create/', views.PedidoCreateView.as_view(), name='pedido-create'),
    path('<int:pk>/update/', views.PedidoUpdateView.as_view(), name='pedido-update'),
    path('<int:pk>/delete/', views.PedidoDeleteView.as_view(), name='pedido-delete'),
]
