from django.urls import path
from .views import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]