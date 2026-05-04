from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class CustomUsuarioAdmin(UserAdmin):

    # Campos exibidos no formulário de criação
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 
                'password1', 
                'password2',
                'tipo_pessoa',
                'telefone',
                'data_nascimento',
                'endereco',
                'cpf',
                'cnpj',
            ),
        }),
    )

    # Campos exibidos na edição do usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {
            'fields': (
                'first_name',
                'last_name',
                'tipo_pessoa',
                'telefone',
                'data_nascimento',
                'endereco',
                'cpf',
                'cnpj',
            )
        }),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Configuração da listagem no admin
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # O email agora é único e usado para login
    model = Usuario


admin.site.register(Usuario, CustomUsuarioAdmin)
