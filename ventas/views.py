# ventas/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Venta
from pagos.models import Pago
from .forms import VentaForm, PagoFormSet, ProductoVentaFormSet, ProductoAlquilerFormSet, PedidoProductoFormSet, SesionFotoFormSet
from django.shortcuts import redirect

class VentaListView(ListView):
    model = Venta
    template_name = 'ventas/venta_list.html'
    context_object_name = 'ventas'

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'ventas/venta_detail.html'
    context_object_name = 'venta'

class VentaCreateView(CreateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('ventas:venta-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['pagos'] = PagoFormSet(self.request.POST)
            data['productos_venta'] = ProductoVentaFormSet(self.request.POST)
            data['productos_alquiler'] = ProductoAlquilerFormSet(self.request.POST)
            data['pedidos'] = PedidoProductoFormSet(self.request.POST)
            data['sesiones_fotos'] = SesionFotoFormSet(self.request.POST)
        else:
            data['pagos'] = PagoFormSet()
            data['productos_venta'] = ProductoVentaFormSet()
            data['productos_alquiler'] = ProductoAlquilerFormSet()
            data['pedidos'] = PedidoProductoFormSet()
            data['sesiones_fotos'] = SesionFotoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pagos = context['pagos']
        productos_venta = context['productos_venta']
        productos_alquiler = context['productos_alquiler']
        pedidos = context['pedidos']
        sesiones_fotos = context['sesiones_fotos']
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user.email
        self.object.save()
        if pagos.is_valid() and productos_venta.is_valid() and productos_alquiler.is_valid() and pedidos.is_valid() and sesiones_fotos.is_valid():
            pagos.instance = self.object
            pagos.save()
            productos_venta.instance = self.object
            productos_venta.save()
            productos_alquiler.instance = self.object
            productos_alquiler.save()
            pedidos.instance = self.object
            pedidos.save()
            sesiones_fotos.instance = self.object
            sesiones_fotos.save()
        return super().form_valid(form)

class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('ventas:venta-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['pagos'] = PagoFormSet(self.request.POST, instance=self.object)
            data['productos_venta'] = ProductoVentaFormSet(self.request.POST, instance=self.object)
            data['productos_alquiler'] = ProductoAlquilerFormSet(self.request.POST, instance=self.object)
            data['pedidos'] = PedidoProductoFormSet(self.request.POST, instance=self.object)
            data['sesiones_fotos'] = SesionFotoFormSet(self.request.POST, instance=self.object)
        else:
            data['pagos'] = PagoFormSet(instance=self.object)
            data['productos_venta'] = ProductoVentaFormSet(instance=self.object)
            data['productos_alquiler'] = ProductoAlquilerFormSet(instance=self.object)
            data['pedidos'] = PedidoProductoFormSet(instance=self.object)
            data['sesiones_fotos'] = SesionFotoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pagos = context['pagos']
        productos_venta = context['productos_venta']
        productos_alquiler = context['productos_alquiler']
        pedidos = context['pedidos']
        sesiones_fotos = context['sesiones_fotos']
        self.object = form.save()
        if pagos.is_valid() and productos_venta.is_valid() and productos_alquiler.is_valid() and pedidos.is_valid() and sesiones_fotos.is_valid():
            pagos.instance = self.object
            pagos.save()
            productos_venta.instance = self.object
            productos_venta.save()
            productos_alquiler.instance = self.object
            productos_alquiler.save()
            pedidos.instance = self.object
            pedidos.save()
            sesiones_fotos.instance = self.object
            sesiones_fotos.save()
        return super().form_valid(form)

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/venta_confirm_delete.html'
    success_url = reverse_lazy('ventas:venta-list')
