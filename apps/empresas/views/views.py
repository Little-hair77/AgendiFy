from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from ..models import Empresa
from ..forms import EmpresaForm, EditarEmpresaForm


class EmpresaListView(ListView):
    model = Empresa
    template_name = 'listar_empresas.html'
    context_object_name = 'empresas'


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'detalhes_empresa.html'
    context_object_name = 'empresa'
    pk_url_kwarg = 'id'


class EmpresaCreateView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'cadastrar_empresa.html'
    success_url = reverse_lazy('listar_empresas')
    success_message = "A empresa foi cadastrada com sucesso!"

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super().form_valid(form)


class EmpresaUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Empresa
    form_class = EditarEmpresaForm
    template_name = 'cadastrar_empresa.html'
    success_url = reverse_lazy('listar_empresas')
    pk_url_kwarg = 'id'
    success_message = "Os dados da empresa foram atualizados com sucesso!"

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'editar'
        return context


class EmpresaDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Empresa
    template_name = 'detalhes_empresa.html'
    success_url = reverse_lazy('listar_empresas')
    pk_url_kwarg = 'id'
    success_message = "A empresa foi removida do sistema com sucesso!"

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'deletar'
        return context