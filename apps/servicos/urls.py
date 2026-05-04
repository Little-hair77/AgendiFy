from django.urls import path
from .views import views

urlpatterns = [
    path('', views.ServicoListView.as_view(), name='listar_servicos'),
    path('cadastro/', views.ServicoCreateView.as_view(), name='cadastrar_servico'),
    path('<int:id>/editar/', views.editar_servico, name='editar_servico'),
    path('<int:id>/deletar/', views.deletar_servico, name='deletar_servico'),
    path('<int:id>/detalhes/', views.detalhes_servico, name='detalhe_servico'),
]