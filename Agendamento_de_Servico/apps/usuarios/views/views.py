from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from ..forms import RegistroUsuarioForm, EditarUsuarioForm

User = get_user_model()

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request, "Usuário registrado com sucesso! Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Erro ao registrar usuário. Verifique os campos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'cadastrar_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.first_name}!")
            return redirect('home') 
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect('login')

def perfil_usuario(request):
    return render(request, 'perfil_usuario.html', {'usuarios': request.user})

def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil_usuario')
        else:
            messages.error(request, "Erro ao atualizar o perfil. Verifique os dados.")
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, 'cadastrar_usuario.html', {
        'usuario': usuario,
        'form': form,
        'modo': 'editar'
    })

def deletar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Conta excluida com sucesso!")
        return redirect('home')
    
    return render(request, 'perfil_usuario.html', {'usuario':usuario, 'modo': 'deletar'})
