from django.urls import path
from views import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('cadastro/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('int:empresa_id/editar/', views.editar_empresa, name='editar_empresa'),
    path('int:empresa_id/deletar/', views.deletar_empresa, name='deletar_empresa'),
]