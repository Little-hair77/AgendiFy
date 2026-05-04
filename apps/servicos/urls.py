from django.urls import path
from .views import views

urlpatterns = [
    path('', views.ServicoListView.as_view(), name='listar_servicos'),
    path('cadastro/', views.ServicoCreateView.as_view(), name='cadastrar_servico'),
    path('<int:id>/editar/', views.ServicoUpdateView.as_view(), name='editar_servico'),
    path('<int:id>/deletar/', views.ServicoDeleteView.as_view(), name='deletar_servico'),
    path('<int:id>/detalhes/', views.ServicoDetailView.as_view(), name='detalhe_servico'),
]