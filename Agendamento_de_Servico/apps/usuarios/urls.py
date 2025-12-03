from django.urls import path
from .views import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('cadastro/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]