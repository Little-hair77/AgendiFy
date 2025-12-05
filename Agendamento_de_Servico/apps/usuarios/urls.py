from django.urls import path
from .views import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cadastro/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('deletar/', views.deletar_usuario, name='deletar_usuario'),
    path('editar/', views.editar_usuario, name='editar_perfil'),
]