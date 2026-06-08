from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'email', 'telefone', 'senha', 'confirmar_senha']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: João da Silva'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'seu@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '(00) 00000-0000'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': '••••••••'
            }),
            'confirmar_senha': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': '••••••••'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        
        return cleaned_data
    
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.username = self.cleaned_data['email']
        usuario.set_password(self. cleaned_data['senha'])
        if commit: 
            usuario.save()
        
        return usuario
    
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'telefone']