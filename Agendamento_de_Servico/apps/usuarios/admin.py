from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
class CustomUsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': ('tipo_pessoa', 'telefone', 'data_nascimento', 'endereco', 'cpf', 'cnpj')
        }),
    )