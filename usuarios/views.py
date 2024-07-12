from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuarios/detalle.html', {'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuarios/')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuarios/')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return HttpResponseRedirect('/usuarios/')
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
