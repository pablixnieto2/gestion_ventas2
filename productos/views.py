from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductoVenta, ProductoAlquiler
from .forms import ProductoVentaForm, ProductoAlquilerForm

def lista_productos(request):
    productos_venta = ProductoVenta.objects.all()
    productos_alquiler = ProductoAlquiler.objects.all()
    return render(request, 'productos/lista.html', {'productos_venta': productos_venta, 'productos_alquiler': productos_alquiler})

def detalle_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

def crear_producto_venta(request):
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoVentaForm()
    return render(request, 'productos/formulario.html', {'form': form})

def editar_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoVentaForm(instance=producto)
    return render(request, 'productos/formulario.html', {'form': form})

def eliminar_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminacion.html', {'producto': producto})

def detalle_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

def crear_producto_alquiler(request):
    if request.method == 'POST':
        form = ProductoAlquilerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoAlquilerForm()
    return render(request, 'productos/formulario.html', {'form': form})

def editar_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    if request.method == 'POST':
        form = ProductoAlquilerForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoAlquilerForm(instance=producto)
    return render(request, 'productos/formulario.html', {'form': form})

def eliminar_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminacion.html', {'producto': producto})
