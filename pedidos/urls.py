from django.urls import path
from .views import PedidoListView, PedidoDetailView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView

app_name = 'pedidos'

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido-list'),
    path('<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('nuevo/', PedidoCreateView.as_view(), name='pedido-create'),
    path('<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido-update'),
    path('<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido-delete'),
]
