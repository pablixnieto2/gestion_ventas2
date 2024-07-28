from django.urls import path
from .views import SesionFotoListView, SesionFotoDetailView, SesionFotoCreateView, SesionFotoUpdateView, SesionFotoDeleteView, get_producto_precio

app_name = 'sesiones_fotos'

urlpatterns = [
    path('', SesionFotoListView.as_view(), name='sesionfoto-list'),
    path('create/', SesionFotoCreateView.as_view(), name='sesionfoto-create'),
    path('<str:pk>/', SesionFotoDetailView.as_view(), name='sesionfoto-detail'),
    path('<str:pk>/update/', SesionFotoUpdateView.as_view(), name='sesionfoto-update'),
    path('<str:pk>/delete/', SesionFotoDeleteView.as_view(), name='sesionfoto-delete'),
    path('api/productos/<uuid:pk>/precio/', get_producto_precio, name='producto-precio'),
]
