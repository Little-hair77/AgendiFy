from rest_framework import viewsets
from apps.empresas.models import Empresa
from apps.profissionais.models import Profissional
from apps.servicos.models  import Servico
from .serializers import EmpresaSerializer, ProfissionalSerializer, ServicoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer