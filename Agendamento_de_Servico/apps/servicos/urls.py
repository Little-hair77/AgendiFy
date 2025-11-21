from django.urls import path
from .views import views

urlpatterns = [
    path('', views.listar_servicos, name='listar_servicos'),
    path('cadastro/', views.cadastrar_servico, name='cadastrar_servico'),
    path('int:servico_id/editar/', views.editar_servico, name='editar_servico'),
    path('int:servico_id/deletar/', views.deletar_servico, name='deletar_servico'),
]