from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView,  DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from ..models import Profissional 
from ..forms import ProfissionalForm
from apps.empresas.models import Empresa


class ProfissionalListView(ListView):
    model = Profissional
    template_name  = 'listar_profissionais.html'
    context_object_name = 'profissionais'

class ProfissionalPorEmpresaListView(ListView):
    model = Profissional
    template_name = 'listar_profissionais.html'
    context_object_name = 'profissionais'

    def get_queryset(self):
        empresa_id = self.kwargs.get('empresa_id')

        return Profissional.objects.filter(empresa_id = empresa_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_id = self.kwargs.get('empresa_id')
        context['empresa'] = get_object_or_404(Empresa, id=empresa_id)

        return context

class ProfissionalCreateView(UserPassesTestMixin,SuccessMessageMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'cadastrar_profissional.html'
    success_message = "Profissional cadastrado com sucesso!"

    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        empresa_id = self.kwargs.get('empresa_id')
        form.instance.empresa_id = empresa_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        empresa_id = self.kwargs.get('empresa_id')
        context['empresa'] = get_object_or_404(Empresa, id=empresa_id)
        
        return context
    
    def get_success_url(self):
        empresa_id = self.kwargs.get('empresa_id')

        return reverse_lazy('listar_profissionais_por_empresa', kwargs={'empresa_id': empresa_id})

class ProfissionalUpdateView(UserPassesTestMixin,SuccessMessageMixin, UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'cadastrar_profissional.html'
    success_message = "Dados do profissional atualizados com sucesso!"

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'editar'
        return  context
     
    def get_success_url(self):
        empresa_id = self.object.empresa.id
        return reverse('listar_profissionais_por_empresa', kwargs = {'empresa_id': empresa_id})

class ProfissionalDetailView (DetailView):
    model = Profissional
    template_name = 'perfil_profissional.html'
    context_object_name = 'profissional'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['modo'] = 'detalhes'
        return context

class ProfissionalDeleteView(UserPassesTestMixin, DeleteView):
    model = Profissional
    template_name = 'perfil_profissional.html'
    context_object_name = 'profissional'
    success_url = reverse_lazy('listar_profissionais')

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['modo'] = 'deletar'
        return context