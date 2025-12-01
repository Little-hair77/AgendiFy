from django.urls import path
from .views import views

urlpatterns = [
    path('', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendar/<int:id>/', views.cadastrar_agendamento, name='cadastrar_agendamento'),
    path('<int:agendamento_id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('<int:agendamento_id>/deletar/', views.deletar_agendamento, name='deletar_agendamento'),
    path('<int:agendamento_id>/detalhes/', views.detalhes_agendamento, name='detalhes_agendamento'),
]
