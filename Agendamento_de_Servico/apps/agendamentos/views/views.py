from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Agendamento
from forms import AgendamentoForm

# Create your views here.
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

def criar_agendamentos(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()

            return redirect('listar_agendamentos')
        else:
            form = AgendamentoForm()
    
    return render(request, 'agendamentos/criar.html', {'form': form})
