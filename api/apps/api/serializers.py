from rest_framework import serializers
from apps.empresas.models import Empresa
from apps.profissionais.models import Profissional
from apps.servicos.models import Servico

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = "__all__"

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = "__all__"