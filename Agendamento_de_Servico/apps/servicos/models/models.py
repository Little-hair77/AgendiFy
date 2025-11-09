from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome