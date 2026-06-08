from django.urls import path
from .views import views

urlpatterns = [
    path('login/', views.UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.UsuarioLogoutView.as_view(), name='logout'),
    path('usuarios/', views.UsuarioListView.as_view(), name='listar_usuarios'),
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastrar_usuario'),
    path('perfil/', views.PefilUsuarioView.as_view(), name='perfil_usuario'),
    path('deletar/', views.UsuarioDeleteView.as_view(), name='deletar_usuario'),
    path('editar/', views.UsuarioUpdateView.as_view(), name='editar_perfil'),
]