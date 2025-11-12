from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def registrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe um usuário com esse e-mail!")
            return redirect('registrar_usuario')
        
        usuario = User.objects.create_user(
            username = email,
            email=email,
            password=senha,
            first_name=nome
        )
        usuario.telefone = telefone
        usuario.save()
        messages.success(request, "Usuário registrado com sucesso! Faça login.")
        return redirect('login_usuario')
    
    return render(request, 'usuarios/registrar.html')

def login_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, "E-mail ou senha inválidos.")
            return redirect('login_usuario')
        
    return render(request, 'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')

def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuarios': request.user})

def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.first_name = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.save()
        messages.success(request, "Informações atualizadas com sucesso!")
        return redirect('perfil_usuario')
    
    return render(request, 'usuarios/editar.html', {'usuario' : usuario})

def deletar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.delete()
        messages.success("Conta excluida com sucesso!")
        return redirect('inicio')
    
    return render(request, 'usuarios/deletar.html')
