from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from apps.agendamentos.models import Agendamento
from apps.empresas.models import Empresa

class DashboardView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            empresas = Empresa.objects.all()
            agendamentos = Agendamento.objects.all()
            
            return render(request, 'dashboard_juridica.html', {
                'empresas': empresas,
                'agendamentos': agendamentos,
                'modo_admin': True
            })

        agendamentos = Agendamento.objects.filter(usuario=user)
        
        return render(request, 'dashboard_fisica.html', {
            'agendamentos': agendamentos
        })