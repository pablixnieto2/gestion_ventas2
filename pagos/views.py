from django.shortcuts import render, get_object_or_404, redirect
from .models import Pago
from .forms import PagoForm

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/lista.html', {'pagos': pagos})

def detalle_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    return render(request, 'pagos/detalle.html', {'pago': pago})

def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pagos')
    else:
        form = PagoForm()
    return render(request, 'pagos/formulario.html', {'form': form})

def editar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('lista_pagos')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'pagos/formulario.html', {'form': form})

def eliminar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        pago.delete()
        return redirect('lista_pagos')
    return render(request, 'pagos/confirmar_eliminacion.html', {'pago': pago})
