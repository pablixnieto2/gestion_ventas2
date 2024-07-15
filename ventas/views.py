from django.shortcuts import render, get_object_or_404, redirect
from .models import Venta
from .forms import VentaForm

def index(request):
    return render(request, 'ventas/index.html')

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_detail(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/venta_detail.html', {'venta': venta})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_edit(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_delete(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})
