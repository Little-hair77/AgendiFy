from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ..forms import LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Usuário ou senha incorretos!")
    
    return render(request, "login.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect('login')

