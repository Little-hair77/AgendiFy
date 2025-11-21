from django.db import models
from apps.empresas.models import Empresa

# Create your models here.
class Tag(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='servicos')
    tags = models.ManyToManyField(Tag, blank=True, related_name='servicos')

    def __str__(self):
        return self.nome