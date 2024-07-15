from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido
from .forms import PedidoForm

def index(request):
    return render(request, 'pedidos/index.html')

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/pedido_form.html', {'form': form})

def pedido_edit(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/pedido_form.html', {'form': form})

def pedido_delete(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido_list')
    return render(request, 'pedidos/pedido_confirm_delete.html', {'pedido': pedido})
