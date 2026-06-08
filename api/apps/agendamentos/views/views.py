from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from apps.servicos.models import Servico
from ..models import Agendamento
from ..forms import AgendamentoForm


class AgendamentoUsuarioListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'listar_agendamentos.html'
    context_object_name = 'agendamentos'

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)


class AgendamentoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'cadastrar_agendamento.html'
    success_url = reverse_lazy('listar_agendamentos_usuario')
    success_message = "Seu agendamento foi realizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Captura o id do serviço vindo da URL para exibir dados na tela se necessário
        context['servico'] = get_object_or_404(Servico, id=self.kwargs.get('servico_id'))
        return context

    def form_valid(self, form):
        servico = get_object_or_404(Servico, id=self.kwargs.get('servico_id'))
        
        form.instance.usuario = self.request.user
        form.instance.servico = servico
        form.instance.empresa = servico.empresa  
        
        return super().form_valid(form)


class AgendamentoDetailView(LoginRequiredMixin, DetailView):
    model = Agendamento
    template_name = 'perfil_agendamentos.html'
    context_object_name = 'agendamento'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)


class AgendamentoUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'cadastrar_agendamento.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listar_agendamentos_usuario')
    success_message = "Agendamento atualizado com sucesso!"

    def test_func(self):
        agendamento = self.get_object()
        return agendamento.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'editar'
        return context


class AgendamentoDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Agendamento
    template_name = 'perfil_agendamentos.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listar_agendamentos_usuario')
    success_message = "Agendamento cancelado com sucesso!"

    def test_func(self):
        # Só permite deletar se o agendamento pertencer ao usuário logado
        agendamento = self.get_object()
        return agendamento.usuario == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'deletar'
        return context


class AgendamentoEmpresaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Agendamento
    template_name = 'listar_agendamentos.html'
    context_object_name = 'agendamentos'

    def test_func(self):
        # Apenas o Administrador Geral pode ter acesso a essa visão macro de relatórios
        return self.request.user.is_authenticated and self.request.user.is_superuser