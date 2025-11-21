from django.db import models
from django.conf import settings

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    endereco = models.CharField(max_length=225)
    telefone = models.CharField()
    email = models.EmailField(unique=True)
    dono = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='empresas'
    )

    def __str__(self):
        return self.nome
    