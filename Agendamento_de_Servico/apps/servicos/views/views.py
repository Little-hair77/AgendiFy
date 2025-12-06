from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Servico
from ..forms import ServicoForm

# Create your views here.
def listar_servicos(request):
    servicos = Servico.objects.all().order_by('nome')

    return render(request, 'listar_servicos.html', {'servicos': servicos})

def cadastrar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_servicos')

    else:
        form = ServicoForm()

    return render(request, 'cadastrar_servico.html', {'form': form})


def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('listar_servicos')
    else:
        form = ServicoForm(instance=servico)

    return render(request, 'cadastrar_servico.html', {
        'form': form,
        'servico': servico,
        'modo': 'editar'
    })

def deletar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        servico.delete()
        return redirect('listar_servicos')

    return render(request, 'detalhes_servico.html', {
        'servico': servico,
        'modo': 'deletar'  # Isso ativa o alerta vermelho no HTML
    })

def detalhes_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    return render(request, 'detalhes_servico.html', {'servico': servico})