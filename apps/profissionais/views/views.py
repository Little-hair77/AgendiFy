from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView,  DeleteView
from django.urls import reverse_lazy
from ..models import Profissional 
from ..forms import ProfissionalForm
from apps.empresas.models import Empresa


class ProfissionalListView(ListView):
    model = Profissional
    template_name  = 'listar_profissional.html'
    context_object_name = 'profissionais'

class ProfissionalPorEmpresaListView(ListView):
    model = Profissional
    template_name = 'listar_profissionais.html'
    context_object_name = 'profissionais'

    def get_queryset(self):
        empresa_id = self.kwargs.get('empresa_id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_id = self.kwargs.get('empresa_id')
        context['empresa'] = get_object_or_404(Empresa, id=empresa_id)

        return context

def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm()

    return render(request, 'cadastrar_profissional.html', {
        'form': form,
        'modo': 'cadastrar'
    })


def editar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm(instance=profissional)
    
    return render(request, 'cadastrar_profissional.html', {
        'form': form,
        'profissional': profissional,
        'modo': 'editar'
    })


def deletar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        profissional.delete()
        return redirect('listar_profissionais')

    return render(request, 'perfil_profissional.html', {
        'profissional': profissional,
        'modo': 'deletar'
    })

def detalhes_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    return render(request, 'perfil_profissional.html', {
        'profissional': profissional,
        'modo': 'detalhes'
    })