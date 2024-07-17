from django.urls import path
from .views import VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView, VentaDeleteView

app_name = 'ventas'

urlpatterns = [
    path('', VentaListView.as_view(), name='venta-list'),
    path('create/', VentaCreateView.as_view(), name='venta-create'),
    path('<str:pk>/', VentaDetailView.as_view(), name='venta-detail'),
    path('<str:pk>/update/', VentaUpdateView.as_view(), name='venta-update'),
    path('<str:pk>/delete/', VentaDeleteView.as_view(), name='venta-delete'),
]
