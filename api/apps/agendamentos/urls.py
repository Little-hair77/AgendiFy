from django.urls import path
from .views import views

urlpatterns = [
    path('agendamentos/', views.AgendamentoUsuarioListView.as_view() , name='listar_agendamentos_usuario'),
    path('agendamentos/', views.AgendamentoEmpresaListView.as_view(), name='listar_agendamentos_empresa'),
    path('agendar/<int:servico_id>/', views.AgendamentoCreateView.as_view(), name='cadastrar_agendamento'),
    path('<int:id>/editar/', views.AgendamentoUpdateView.as_view(), name='editar_agendamento'),
    path('<int:id>/deletar/', views.AgendamentoDeleteView.as_view(), name='deletar_agendamento'),
    path('<int:id>/detalhes/', views.AgendamentoDetailView.as_view(), name='detalhes_agendamento'),
]
