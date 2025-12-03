from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.servicos.models import Servico
from ..models import Agendamento
from ..forms import AgendamentoForm

# Create your views here.
@login_required
def listar_agendamentos_usuario(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'listar_agedamentos.html', {'agendamentos': agendamentos})

@login_required
def listar_agendamentos_empresa(request):
    agendamentos = Agendamento.objects.filter(
        servico__empresa__dono=request.user
    )
    return render(request, 'listar_agendamentos_empresa.html', {'agendamentos': agendamentos})

@login_required
def cadastrar_agendamento(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.servico = servico
            agendamento.save()
            return redirect('listar_agendamentos')

    else:
        form = AgendamentoForm()

    return render(request, 'cadastrar_agendamento.html', {
        'form': form,
        'servico': servico
    })

@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, usuario=request.user)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, 'cadastrar_agendamento.html', {
        'form': form,
        'agendamento': agendamento
    })

@login_required
def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')

@login_required
def detalhes_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    return render(request, 'perfil_agendamentos.html', {'agendamento': agendamento})