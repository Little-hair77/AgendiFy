from django.urls import path
from .views import views

urlpatters = [
    path('', views.dashboard, name='dashboard'),
]