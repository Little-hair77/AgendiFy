from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'cargo', 'servicos', 'ativo']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'cargo' : forms.TextInput(attrs={'class':'form-control'}),
            'servicos' : forms.SelectMultiple(attrs={'class':'form-select'}),
            'ativo' : forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nome' : 'Nome do Profissional',
            'cargo' : 'Cargo / Função',
            'servicos' : 'Serviços realizados',
            'ativo' : 'Ativo',
        }