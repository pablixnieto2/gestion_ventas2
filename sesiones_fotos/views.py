from django.shortcuts import render, get_object_or_404, redirect
from .models import SesionFotos
from .forms import SesionFotosForm

def lista_sesiones_fotos(request):
    sesiones_fotos = SesionFotos.objects.all()
    return render(request, 'sesiones_fotos/lista.html', {'sesiones_fotos': sesiones_fotos})

def detalle_sesion_foto(request, pk):
    sesion_foto = get_object_or_404(SesionFotos, pk=pk)
    return render(request, 'sesiones_fotos/detalle.html', {'sesion_foto': sesion_foto})

def crear_sesion_foto(request):
    if request.method == 'POST':
        form = SesionFotosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sesiones_fotos')
    else:
        form = SesionFotosForm()
    return render(request, 'sesiones_fotos/formulario.html', {'form': form})

def editar_sesion_foto(request, pk):
    sesion_foto = get_object_or_404(SesionFotos, pk=pk)
    if request.method == 'POST':
        form = SesionFotosForm(request.POST, instance=sesion_foto)
        if form.is_valid():
            form.save()
            return redirect('lista_sesiones_fotos')
    else:
        form = SesionFotosForm(instance=sesion_foto)
    return render(request, 'sesiones_fotos/formulario.html', {'form': form})

def eliminar_sesion_foto(request, pk):
    sesion_foto = get_object_or_404(SesionFotos, pk=pk)
    if request.method == 'POST':
        sesion_foto.delete()
        return redirect('lista_sesiones_fotos')
    return render(request, 'sesiones_fotos/confirmar_eliminacion.html', {'sesion_foto': sesion_foto})
