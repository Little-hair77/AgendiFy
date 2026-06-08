from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from ..forms import RegistroUsuarioForm, EditarUsuarioForm
from ..models import Usuario

User = get_user_model()

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'listar_usuarios.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    template_name  = 'cadastrar_usuario.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')

    success_message = "Usuário registrado com sucesso! Faça Login."

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao registrar o usuário. Verifique os campos.")

        return super().form_invalid(form)

class UsuarioLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.get_user()

        messages.success(self.request, f"Bem-vindo, {user.first_name}!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha inválidos.")
        return super().form_invalid(form)

class UsuarioLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            messages.info(request, "Você saiu da sua conta com sucesso. Até logo!")
            
        return super().dispatch(request, *args, **kwargs)

class PefilUsuarioView(LoginRequiredMixin, TemplateView):
    template_name =  'perfil_usuario.html'

class UsuarioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'cadastrar_usuario.html'
    success_url = reverse_lazy('perfil_usuario')
    success_message = "Seus dados foram atualizados com sucesso!"

    fields = ['first_name', 'email', 'telefone']

    def get_object(self, queryset = None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['modo'] = 'editar'
        return context

class UsuarioDeleteView(UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'pefil_usuario'
    success_url = reverse_lazy('lista_usuarios')
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo'] = 'deletar'
        context['usuario'] = self.object

        return  context
    
    def form_valid(self, form):
        messages.success(self.request, "Usuário excluído com sucesso do sistema!")
        return super().form_valid(form)