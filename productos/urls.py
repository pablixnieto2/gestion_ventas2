from django.urls import path
from .views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

app_name = 'productos'

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('create/', ProductoCreateView.as_view(), name='producto-create'),
    path('<uuid:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('<uuid:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('<uuid:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),
]
