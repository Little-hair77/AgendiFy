from django.urls import path
from .views import views

urlpatterns = [
    path('', views.listar_profissionais, name='listar_profissionais'),
    path('novo/', views.cadastrar_profissional, name='cadastrar_profissional'),
    path('<int:pk>/editar/', views.editar_profissional, name='editar_profissional'),
    path('<int:pk>/deletar/', views.deletar_profissional, name='deletar_profissional'),
]