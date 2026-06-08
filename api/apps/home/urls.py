from django.urls import path
from .views import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('contato/', views.ContatoTemplateView.as_view(), name='contato'),
]