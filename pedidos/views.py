from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pedido, PedidoProducto
from .forms import PedidoForm, PedidoProductoForm
from django.forms import inlineformset_factory
from django.shortcuts import redirect

PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1)

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/pedido_list.html'
    context_object_name = 'pedidos'

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedidos/pedido_detail.html'

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedidos:pedido-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['productos'] = PedidoProductoFormSet(self.request.POST)
        else:
            data['productos'] = PedidoProductoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        productos = context['productos']
        if form.is_valid() and productos.is_valid():
            self.object = form.save()
            productos.instance = self.object
            productos.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedidos:pedido-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['productos'] = PedidoProductoFormSet(self.request.POST, instance=self.object)
        else:
            data['productos'] = PedidoProductoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        productos = context['productos']
        if form.is_valid() and productos.is_valid():
            self.object = form.save()
            productos.instance = self.object
            productos.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedidos/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedidos:pedido-list')
