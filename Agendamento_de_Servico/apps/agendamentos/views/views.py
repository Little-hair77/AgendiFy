from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Agendamento
from forms import AgendamentoForm

# Create your views here.
@login_required
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'templates/listar.html', {'agendamentos': agendamentos})

@login_required
def cadastrar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()

            return redirect('listar_agendamentos')
        else:
            form = AgendamentoForm()
    
    return render(request, 'templates/criar.html', {'form': form})

@login_required
def editar_agendamento(request):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
   
    if request.method == 'POST':
        form = Agendamento(request.POST, instance=agendamento)

        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
        else:
            form = AgendamentoForm(instance=agendamento)

    return render(request, 'templates/editar.html', {'form': form, 'agendamento': agendamento})

@login_required
def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')

@login_required
def detalhes_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    return render(request, 'templates/detalhes.html', {'agendamento': agendamento})