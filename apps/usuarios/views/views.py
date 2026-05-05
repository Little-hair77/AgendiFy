from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
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

def perfil_usuario(request):
    return render(request, 'perfil_usuario.html', {'usuarios': request.user})

def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil_usuario')
        else:
            messages.error(request, "Erro ao atualizar o perfil. Verifique os dados.")
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, 'cadastrar_usuario.html', {
        'usuario': usuario,
        'form': form,
        'modo': 'editar'
    })

def deletar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Conta excluida com sucesso!")
        return redirect('home')
    
    return render(request, 'perfil_usuario.html', {'usuario':usuario, 'modo': 'deletar'})
