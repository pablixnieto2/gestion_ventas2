from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

@login_required
def detalle_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    return render(request, 'usuarios/detalle.html', {'usuario': usuario})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/formulario.html', {'form': form})

@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = CustomUserChangeForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form})

@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminacion.html', {'usuario': usuario})
