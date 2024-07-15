from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pago
from .forms import PagoForm

def index(request):
    return render(request, 'pagos/index.html')

def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/pago_list.html', {'pagos': pagos})

def pago_detail(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    return render(request, 'pagos/pago_detail.html', {'pago': pago})

def pago_create(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pago_list'))
    else:
        form = PagoForm()
    return render(request, 'pagos/pago_form.html', {'form': form})

def pago_update(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    if request.method == "POST":
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pago_list'))
    else:
        form = PagoForm(instance=pago)
    return render(request, 'pagos/pago_form.html', {'form': form})

def pago_delete(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    if request.method == "POST":
        pago.delete()
        return HttpResponseRedirect(reverse('pago_list'))
    return render(request, 'pagos/pago_confirm_delete.html', {'pago': pago})
