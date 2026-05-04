from django.urls import path
from .views import views

urlpatterns = [
    path('agendamentos/', views.listar_agendamentos_usuario , name='listar_agendamentos_usuario'),
    path('agendamentos/', views.listar_agendamentos_empresa, name='listar_agendamentos_empresa'),
    path('agendar/<int:id>/', views.cadastrar_agendamento, name='cadastrar_agendamento'),
    path('<int:id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('<int:id>/deletar/', views.deletar_agendamento, name='deletar_agendamento'),
    path('<int:id>/detalhes/', views.detalhes_agendamento, name='detalhes_agendamento'),
]
