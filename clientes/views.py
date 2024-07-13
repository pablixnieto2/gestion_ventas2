from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente_list'))
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente_list'))
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == "POST":
        cliente.delete()
        return HttpResponseRedirect(reverse('cliente_list'))
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})
