from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

def producto_detail(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    return render(request, 'productos/producto_detail.html', {'producto': producto})

def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('producto_list'))
    else:
        form = ProductoForm()
    return render(request, 'productos/producto_form.html', {'form': form})

def producto_update(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('producto_list'))
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_form.html', {'form': form})

def producto_delete(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == "POST":
        producto.delete()
        return HttpResponseRedirect(reverse('producto_list'))
    return render(request, 'productos/producto_confirm_delete.html', {'producto': producto})
