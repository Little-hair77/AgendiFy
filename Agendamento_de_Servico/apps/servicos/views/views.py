from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Servico
from forms import ServicoForm

# Create your views here.
def listar_servicos(request):
    servicos = Servico.objects.all().order_by('nome')

    return render(request, 'servicos/listar.html', {'servicos': servicos})

def criar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_servicos')
        else:
            form = ServicoForm()

    return render(request, 'servicos/listar.html', {'form': form})

def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)

        if form.is_valid():
            form.save()
            return redirect('listar_servicos')
        else:
            form = ServicoForm(instance=servico)

    return render(request, 'servicos/editar.html', {'form': form, 'servico': servico})

def excluir_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()

    return redirect('listar_servicos')

def detalhes_servico(request, id):
    servico = get_object_or_404(Servico, id)

    return render(request, 'servicos/detalhes.html', {'servico': servico})