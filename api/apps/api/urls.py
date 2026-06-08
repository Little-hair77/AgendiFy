from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'profissionais', views.ProfissionalViewSet)
router.register(r'servicos', views.ServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]