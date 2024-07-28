from django.urls import path
from .views import PagoListView, PagoDetailView, PagoCreateView, PagoUpdateView, PagoDeleteView

app_name = 'pagos'

urlpatterns = [
    path('', PagoListView.as_view(), name='pago-list'),
    path('<int:pk>/', PagoDetailView.as_view(), name='pago-detail'),
    path('create/', PagoCreateView.as_view(), name='pago-create'),
    path('<int:pk>/update/', PagoUpdateView.as_view(), name='pago-update'),
    path('<int:pk>/delete/', PagoDeleteView.as_view(), name='pago-delete'),
]
