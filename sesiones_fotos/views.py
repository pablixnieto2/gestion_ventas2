from django.shortcuts import render, get_object_or_404, redirect
from .models import SesionFoto
from .forms import SesionFotoForm

def index(request):
    return render(request, 'sesiones_fotos/index.html')

def sesion_foto_list(request):
    sesiones_fotos = SesionFoto.objects.all()
    return render(request, 'sesiones_fotos/sesion_foto_list.html', {'sesiones_fotos': sesiones_fotos})

def sesion_foto_detail(request, id):
    sesion_foto = get_object_or_404(SesionFoto, id=id)
    return render(request, 'sesiones_fotos/sesion_foto_detail.html', {'sesion_foto': sesion_foto})

def sesion_foto_create(request):
    if request.method == 'POST':
        form = SesionFotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion_foto_list')
    else:
        form = SesionFotoForm()
    return render(request, 'sesiones_fotos/sesion_foto_form.html', {'form': form})

def sesion_foto_edit(request, id):
    sesion_foto = get_object_or_404(SesionFoto, id=id)
    if request.method == 'POST':
        form = SesionFotoForm(request.POST, instance=sesion_foto)
        if form.is_valid():
            form.save()
            return redirect('sesion_foto_list')
    else:
        form = SesionFotoForm(instance=sesion_foto)
    return render(request, 'sesiones_fotos/sesion_foto_form.html', {'form': form})

def sesion_foto_delete(request, id):
    sesion_foto = get_object_or_404(SesionFoto, id=id)
    if request.method == 'POST':
        sesion_foto.delete()
        return redirect('sesion_foto_list')
    return render(request, 'sesiones_fotos/sesion_foto_confirm_delete.html', {'sesion_foto': sesion_foto})
