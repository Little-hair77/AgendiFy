from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):

    TIPO_PESSOA_CHOICES=[
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)

    @property
    def nome_completo(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def __str__(self):
        if self.tipo_pessoa == 'F':
            return self.nome_completo or self.username
        return f"{self.username} (PJ)"
