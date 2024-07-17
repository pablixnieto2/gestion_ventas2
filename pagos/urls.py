# pagos/urls.py

from django.urls import path
from . import views

app_name = 'pagos'

urlpatterns = [
    path('', views.PagoListView.as_view(), name='pago-list'),
    path('<int:pk>/', views.PagoDetailView.as_view(), name='pago-detail'),
    path('create/', views.PagoCreateView.as_view(), name='pago-create'),
    path('<int:pk>/update/', views.PagoUpdateView.as_view(), name='pago-update'),
    path('<int:pk>/delete/', views.PagoDeleteView.as_view(), name='pago-delete'),
]
