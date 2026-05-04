from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from ..models import Servico
from ..forms import ServicoForm

# Create your views here.
class ServicoListView(ListView):
    model = Servico
    template_name = 'listar_servicos.html'
    context_object_name = 'servicos'

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'cadastrar_servico.html'

    success_url = reverse_lazy('listar_servicos')


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
        'modo': 'deletar'  
    })

def detalhes_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    return render(request, 'detalhes_servico.html', {'servico': servico})