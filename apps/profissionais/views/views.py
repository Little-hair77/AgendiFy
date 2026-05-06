from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView,  DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
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

        return Profissional.objects.filter(empresa_id = empresa_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_id = self.kwargs.get('empresa_id')
        context['empresa'] = get_object_or_404(Empresa, id=empresa_id)

        return context

class ProfissionalCreateView(UserPassesTestMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'cadastrar_profissional.html'
    success_message = "Profissional cadastrado com sucesso!"

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_id = self.kwargs.get('empresa_id')
        context['empresa'] = get_object_or_404(Empresa, id=empresa_id)

        return context
    
    def form_valid(self, form):
        empresa = get_object_or_404(Empresa, id=self.kwargs.get('empresa_id'))
        
        form.isinstance.empresa = empresa

        return super().form_valid(form)
    
    def get_sucess_url(self):
        empresa_id = self.kwargs.get('empresa_id')

        return reverse_lazy('listar_profissionais_por_empresa', kwargs={'empresa_id': empresa_id})

class ProfissionalUpdateView(UserPassesTestMixin,UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'cadastrar_profissional.html'
    success_message = "Dados do profissional atualizados com sucesso!"
    pk_url_kwarg = 'id'

    def test_func(self):
        return super().request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'editar'
        return  context
     
    def get_success_url(self):
        empresa_id = self.object.empresa.id
        return reverse_lazy('listar_profissionais_por_empresa', kwargs = {'empresa_id': empresa_id})

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