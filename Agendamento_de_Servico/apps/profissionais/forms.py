from django import forms
from .models.models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'cargo', 'empresa', 'servicos', 'ativo']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'cargo' : forms.TextInput(attrs={'class':'form-control'}),
            'empresa' : forms.Select(attrs={'class':'form-select'}),
            'servicos' : forms.SelectMultiple(attrs={'class':'form-select'}),
            'ativo' : forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nome' : 'Nome do Profissional',
            'cargo' : 'Cargo / Função',
            'empresa' : 'Empresa',
            'servicos' : 'Serviços realizados',
            'ativo' : 'Ativo',
        }