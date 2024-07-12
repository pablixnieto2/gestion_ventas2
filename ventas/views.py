from django.shortcuts import render, get_object_or_404, redirect
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista.html', {'ventas': ventas})

def detalle_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'ventas/detalle.html', {'venta': venta})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/formulario.html', {'form': form})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/formulario.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'ventas/confirmar_eliminacion.html', {'venta': venta})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista.html', {'ventas': ventas})

def detalle_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'ventas/detalle.html', {'venta': venta})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/formulario.html', {'form': form})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/formulario.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'ventas/confirmar_eliminacion.html', {'venta': venta})
