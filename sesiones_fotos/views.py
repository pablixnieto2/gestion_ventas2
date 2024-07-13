from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SesionFoto
from .forms import SesionFotoForm

def sesionfoto_list(request):
    sesiones = SesionFoto.objects.all()
    return render(request, 'sesiones_fotos/sesionfoto_list.html', {'sesiones': sesiones})

def sesionfoto_detail(request, id):
    sesion = get_object_or_404(SesionFoto, id_sesion=id)
    return render(request, 'sesiones_fotos/sesionfoto_detail.html', {'sesion': sesion})

def sesionfoto_create(request):
    if request.method == "POST":
        form = SesionFotoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sesionfoto_list'))
    else:
        form = SesionFotoForm()
    return render(request, 'sesiones_fotos/sesionfoto_form.html', {'form': form})

def sesionfoto_update(request, id):
    sesion = get_object_or_404(SesionFoto, id_sesion=id)
    if request.method == "POST":
        form = SesionFotoForm(request.POST, instance=sesion)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sesionfoto_list'))
    else:
        form = SesionFotoForm(instance=sesion)
    return render(request, 'sesiones_fotos/sesionfoto_form.html', {'form': form})

def sesionfoto_delete(request, id):
    sesion = get_object_or_404(SesionFoto, id_sesion=id)
    if request.method == "POST":
        sesion.delete()
        return HttpResponseRedirect(reverse('sesionfoto_list'))
    return render(request, 'sesiones_fotos/sesionfoto_confirm_delete.html', {'sesion': sesion})
