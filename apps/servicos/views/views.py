from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from ..models import Servico
from ..forms import ServicoForm

# Create your views here.
class ServicoListView(ListView):
    model = Servico
    template_name = 'listar_servicos.html'
    context_object_name = 'servicos'

class ServicoCreateView(UserPassesTestMixin,CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'cadastrar_servico.html'

    success_url = reverse_lazy('listar_servicos')

    def test_func(self):
        # Garante que Apenas o SuperUser possa cadastrar
        return self.request.user.is_superuser

class ServicoUpdateView(UserPassesTestMixin,UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'cadastrar_servico.html'
    success_url = reverse_lazy('listar_servicos')
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'editar'
        return context
    
class ServicoDeleteView(UserPassesTestMixin,DeleteView):
    model = Servico
    template_name = 'detalhes_servico.html'
    success_url = reverse_lazy('listar_servicos')
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'deletar'
        context['servico'] = self.get_object
        return context

def detalhes_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    return render(request, 'detalhes_servico.html', {'servico': servico})