from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    usuario = request.user

    if usuario.tipo_pessoa == "F":
        template = 'dashboard_cliente.html'
    else:
        template = 'dashboard_empresa.html'
    
    return render(request, template, {'usuario': usuario})