from django.db import models
from django.conf import settings
from django.models import Empresa
from django.models import Servico

# Create your models here.
class Agendamento(models.Model):
    STATUS_CHOICES=[
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído')
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizaado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.servico.nome} ({self.data_hora.strftime('%d/%m/%Y %H:%M')})"