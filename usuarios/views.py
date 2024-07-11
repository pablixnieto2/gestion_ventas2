from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
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
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            Usuario.objects.create(user=user, telefono=request.POST['telefono'])
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario.user)
        if form.is_valid():
            usuario.user.username = form.cleaned_data['username']
            usuario.user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                usuario.user.set_password(form.cleaned_data['password'])
            usuario.user.save()
            usuario.telefono = request.POST['telefono']
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario.user)
    return render(request, 'usuarios/formulario.html', {'form': form, 'telefono': usuario.telefono})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.user.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminacion.html', {'usuario': usuario})
