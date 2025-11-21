from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from usuarios.forms import RegistroUsuarioForm, EditarUsuarioForm

User = get_user_model()

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request, "Usuário registrado com sucesso! Faça login.")
            return redirect('login_usuario')
        else:
            messages.error(request, "Erro ao registrar usuário. Verifique os campos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'templates/registrar.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.first_name}!")
            return redirect('inicio')
        else:
            messages.error(request, "E-mail ou senha inválidos.")
        
    return render(request, 'templates/login.html')

def logout_usuario(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect('login_usuario')

def perfil_usuario(request):
    return render(request, 'templates/perfil.html', {'usuarios': request.user})

def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = EditarUsuarioForm(request, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")        
            return redirect('perfil_usuario')
        else:
            messages.error(request, "Erro ao atualizar o perfil. Verifique os dados.")
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, 'templates/editar.html', {'usuario' : usuario})

def deletar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.delete()
        messages.success("Conta excluida com sucesso!")
        return redirect('inicio')
    
    return render(request, 'templates/deletar.html')
