from django.urls import path
from .views import views

urlpatterns = [
    path('', views.ProfissionalListView.as_view(), name='listar_profissionais'),
    path('novo/', views.cadastrar_profissional, name='cadastrar_profissional'),
    path('<int:pk>/editar/', views.editar_profissional, name='editar_profissional'),
    path('<int:pk>/deletar/', views.deletar_profissional, name='deletar_profissional'),
    path('<int:pk>/detalhes/', views.detalhes_profissional, name='detalhes_profissional'),
    path('profissionais/empresa/<int:empresa_id>/', views.ProfissionalPorEmpresaListView.as_view(), name='listar_profissionais_por_empresa'),
]