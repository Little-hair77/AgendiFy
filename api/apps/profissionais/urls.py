from django.urls import path
from .views import views

urlpatterns = [
    path('', views.ProfissionalListView.as_view(), name='listar_profissionais'),
    path('empresa/<int:empresa_id>/cadastrar/', views.ProfissionalCreateView.as_view(), name='cadastrar_profissional'),
    path('<int:pk>/editar/', views.ProfissionalUpdateView.as_view(), name='editar_profissional'),
    path('<int:pk>/deletar/', views.ProfissionalDeleteView.as_view(), name='deletar_profissional'),
    path('<int:pk>/detalhes/', views.ProfissionalDetailView.as_view(), name='detalhes_profissional'),
    path('profissionais/empresa/<int:empresa_id>/', views.ProfissionalPorEmpresaListView.as_view(), name='listar_profissionais_por_empresa'),
]