from django.shortcuts import render, get_object_or_404, redirect
from .models import SesionFotos
from .forms import SesionFotosForm

def lista_sesiones_fotos(request):
    sesiones = SesionFotos.objects.all()
    return render(request, 'sesiones_fotos/lista.html', {'sesiones': sesiones})

def detalle_sesion_fotos(request, pk):
    sesion = get_object_or_404(SesionFotos, pk=pk)
    return render(request, 'sesiones_fotos/detalle.html', {'sesion': sesion})

def crear_sesion_fotos(request):
    if request.method == 'POST':
        form = SesionFotosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_sesiones_fotos')
    else:
        form = SesionFotosForm()
    return render(request, 'sesiones_fotos/formulario.html', {'form': form})

def editar_sesion_fotos(request, pk):
    sesion = get_object_or_404(SesionFotos, pk=pk)
    if request.method == 'POST':
        form = SesionFotosForm(request.POST, request.FILES, instance=sesion)
        if form.is_valid():
            form.save()
            return redirect('lista_sesiones_fotos')
    else:
        form = SesionFotosForm(instance=sesion)
    return render(request, 'sesiones_fotos/formulario.html', {'form': form})

def eliminar_sesion_fotos(request, pk):
    sesion = get_object_or_404(SesionFotos, pk=pk)
    if request.method == 'POST':
        sesion.delete()
        return redirect('lista_sesiones_fotos')
    return render(request, 'sesiones_fotos/confirmar_eliminacion.html', {'sesion': sesion})
