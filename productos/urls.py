from django.urls import path
from .views import ProductoVentaListView, ProductoAlquilerListView, ProductoDetailView, ProductoVentaCreateView, ProductoVentaUpdateView, ProductoVentaDeleteView, ProductoAlquilerCreateView, ProductoAlquilerUpdateView, ProductoAlquilerDeleteView, get_producto_precio

app_name = 'productos'

urlpatterns = [
    path('ventas/', ProductoVentaListView.as_view(), name='producto-venta-list'),
    path('alquileres/', ProductoAlquilerListView.as_view(), name='producto-alquiler-list'),
    path('detalle/<uuid:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('venta/nuevo/', ProductoVentaCreateView.as_view(), name='producto-venta-create'),
    path('venta/<uuid:pk>/editar/', ProductoVentaUpdateView.as_view(), name='producto-venta-update'),
    path('venta/<uuid:pk>/eliminar/', ProductoVentaDeleteView.as_view(), name='producto-venta-delete'),
    path('alquiler/nuevo/', ProductoAlquilerCreateView.as_view(), name='producto-alquiler-create'),
    path('alquiler/<uuid:pk>/editar/', ProductoAlquilerUpdateView.as_view(), name='producto-alquiler-update'),
    path('alquiler/<uuid:pk>/eliminar/', ProductoAlquilerDeleteView.as_view(), name='producto-alquiler-delete'),
    path('api/productos/<uuid:pk>/precio/', get_producto_precio, name='producto-precio'),
]
