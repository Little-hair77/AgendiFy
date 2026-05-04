from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.agendamentos.models import Agendamento
from apps.empresas.models import Empresa

# Create your views here.
@login_required
def dashboard(request):

    user = request.user

    # Pessoa Física → visualizar agendamentos feitos por ela
    if user.tipo_pessoa == 'F':
        agendamentos = Agendamento.objects.filter(usuario=user)
        return render(request, 'dashboard_fisica.html', {
            'agendamentos': agendamentos
        })

    # Pessoa Jurídica → visualizar empresa(s) e agendamentos recebidos
    if user.tipo_pessoa == 'J':
        empresas = Empresa.objects.filter(dono=user)

        # Se quiser listar todos agendamentos da empresa:
        agendamentos = Agendamento.objects.filter(empresa__in=empresas)

        return render(request, 'dashboard_juridica.html', {
            'empresas': empresas,
            'agendamentos': agendamentos
        })

    return render(request, 'dashboard_fisica.html')