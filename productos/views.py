from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductoVenta, ProductoAlquiler
from .forms import ProductoVentaForm, ProductoAlquilerForm

# Producto Venta
def lista_productos_venta(request):
    productos = ProductoVenta.objects.all()
    return render(request, 'productos/lista_venta.html', {'productos': productos})

def detalle_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    return render(request, 'productos/detalle_venta.html', {'producto': producto})

def crear_producto_venta(request):
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos_venta')
    else:
        form = ProductoVentaForm()
    return render(request, 'productos/formulario_venta.html', {'form': form})

def editar_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos_venta')
    else:
        form = ProductoVentaForm(instance=producto)
    return render(request, 'productos/formulario_venta.html', {'form': form})

def eliminar_producto_venta(request, pk):
    producto = get_object_or_404(ProductoVenta, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos_venta')
    return render(request, 'productos/confirmar_eliminacion_venta.html', {'producto': producto})

# Producto Alquiler
def lista_productos_alquiler(request):
    productos = ProductoAlquiler.objects.all()
    return render(request, 'productos/lista_alquiler.html', {'productos': productos})

def detalle_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    return render(request, 'productos/detalle_alquiler.html', {'producto': producto})

def crear_producto_alquiler(request):
    if request.method == 'POST':
        form = ProductoAlquilerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos_alquiler')
    else:
        form = ProductoAlquilerForm()
    return render(request, 'productos/formulario_alquiler.html', {'form': form})

def editar_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    if request.method == 'POST':
        form = ProductoAlquilerForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos_alquiler')
    else:
        form = ProductoAlquilerForm(instance=producto)
    return render(request, 'productos/formulario_alquiler.html', {'form': form})

def eliminar_producto_alquiler(request, pk):
    producto = get_object_or_404(ProductoAlquiler, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos_alquiler')
    return render(request, 'productos/confirmar_eliminacion_alquiler.html', {'producto': producto})
