from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SesionFoto
from .forms import SesionFotoForm
from productos.models import ProductoVenta
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator

class SesionFotoListView(ListView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_list.html'
    context_object_name = 'sesiones_fotos'

class SesionFotoDetailView(DetailView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_detail.html'

class SesionFotoCreateView(CreateView):
    model = SesionFoto
    form_class = SesionFotoForm
    template_name = 'sesiones_fotos/sesionfoto_form.html'
    success_url = reverse_lazy('sesiones_fotos:sesionfoto-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        return super().form_valid(form)

class SesionFotoUpdateView(UpdateView):
    model = SesionFoto
    form_class = SesionFotoForm
    template_name = 'sesiones_fotos/sesionfoto_form.html'
    success_url = reverse_lazy('sesiones_fotos:sesionfoto-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        return super().form_valid(form)

class SesionFotoDeleteView(DeleteView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_confirm_delete.html'
    success_url = reverse_lazy('sesiones_fotos:sesionfoto-list')

@method_decorator(require_GET, name='dispatch')
def get_producto_precio(request, pk):
    try:
        producto = ProductoVenta.objects.get(pk=pk)
        return JsonResponse({'precio': producto.pvp})
    except ProductoVenta.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
