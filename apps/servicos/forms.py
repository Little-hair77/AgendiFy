from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['empresa', 'nome', 'descricao', 'preco', 'tags']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do serviço'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva o serviço oferecido'
            }),
            'preco': forms.NumberInput(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-select'})
        }
        labels = {
            'empresa': 'Empresa responsável',
            'nome': 'Nome do serviço',
            'descricao': 'Descrição',
            'preco': 'Preço (R$)',
            'tags': 'Tags (opicional)'
        }