from django.db import models
from apps.empresas.models import Empresa
from apps.servicos.models import Servico

# Create your models here.
class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True)
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='profissionais'
    )

    servicos = models.ManyToManyField(
        Servico,
        related_name='profissionais',
        blank=True
    )

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"
