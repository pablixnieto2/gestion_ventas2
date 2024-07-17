from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Venta
from .forms import VentaForm, PagoFormSet
from productos.models import Producto

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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['productos'].queryset = Producto.objects.filter(estado='Activo')  # Filtrar productos activos
        return form

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['pagos'] = PagoFormSet(self.request.POST)
        else:
            data['pagos'] = PagoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pagos = context['pagos']
        self.object = form.save()
        if pagos.is_valid():
            pagos.instance = self.object
            pagos.save()
        return super().form_valid(form)

class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('ventas:venta-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['productos'].queryset = Producto.objects.filter(estado='Activo')
        return form

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['pagos'] = PagoFormSet(self.request.POST, instance=self.object)
        else:
            data['pagos'] = PagoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pagos = context['pagos']
        self.object = form.save()
        if pagos.is_valid():
            pagos.instance = self.object
            pagos.save()
        return super().form_valid(form)

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/venta_confirm_delete.html'
    success_url = reverse_lazy('ventas:venta-list')
