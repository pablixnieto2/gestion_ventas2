from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Producto, ProductoVenta, ProductoAlquiler
from .forms import ProductoVentaForm, ProductoAlquilerForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET


class ProductoVentaListView(ListView):
    model = ProductoVenta
    template_name = 'productos/producto_venta_list.html'
    context_object_name = 'productos_venta'

class ProductoAlquilerListView(ListView):
    model = ProductoAlquiler
    template_name = 'productos/producto_alquiler_list.html'
    context_object_name = 'productos_alquiler'

class ProductoDetailView(DetailView):
    model = Producto  # Cambia a Producto para manejar ambos tipos de productos
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'

    def get_object(self):
        try:
            return ProductoVenta.objects.get(pk=self.kwargs['pk'])
        except ProductoVenta.DoesNotExist:
            return ProductoAlquiler.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if isinstance(self.object, ProductoAlquiler):
            context['cantidad'] = self.object.cantidad
        elif isinstance(self.object, ProductoVenta):
            context['stock'] = {self.object.tienda: self.object.stock}
        return context

class ProductoVentaCreateView(CreateView):
    model = ProductoVenta
    template_name = 'productos/producto_venta_form.html'
    form_class = ProductoVentaForm
    success_url = reverse_lazy('productos:producto-venta-list')

class ProductoVentaUpdateView(UpdateView):
    model = ProductoVenta
    template_name = 'productos/producto_venta_form.html'
    form_class = ProductoVentaForm
    success_url = reverse_lazy('productos:producto-venta-list')

class ProductoVentaDeleteView(DeleteView):
    model = ProductoVenta
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('productos:producto-venta-list')

class ProductoAlquilerCreateView(CreateView):
    model = ProductoAlquiler
    template_name = 'productos/producto_alquiler_form.html'
    form_class = ProductoAlquilerForm
    success_url = reverse_lazy('productos:producto-alquiler-list')

class ProductoAlquilerUpdateView(UpdateView):
    model = ProductoAlquiler
    template_name = 'productos/producto_alquiler_form.html'
    form_class = ProductoAlquilerForm
    success_url = reverse_lazy('productos:producto-alquiler-list')

class ProductoAlquilerDeleteView(DeleteView):
    model = ProductoAlquiler
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('productos:producto-alquiler-list')

@require_GET
def get_producto_precio(request, pk):
    try:
        producto = ProductoVenta.objects.get(pk=pk)
        return JsonResponse({'precio': producto.pvp})
    except ProductoVenta.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)