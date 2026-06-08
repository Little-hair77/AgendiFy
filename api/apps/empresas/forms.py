from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'descricao', 'endereco', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }

class EditarEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'descricao', 'endereco', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }