from django.urls import path
from .views import views

urlpatterns = [
    path('', views.EmpresaListView.as_view(), name='listar_empresas'),
    path('cadastro/', views.EmpresaCreateView.as_view(), name='cadastrar_empresa'),
    path('<int:id>/editar/', views.EmpresaUpdateView.as_view(), name='editar_empresa'),
    path('<int:id>/deletar/', views.EmpresaDeleteView.as_view(), name='deletar_empresa'),
    path('<int:id>/detalhes/', views.EmpresaDetailView.as_view(), name='detalhes_empresa'),
]