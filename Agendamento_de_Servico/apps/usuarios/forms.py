from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'email', 'telefone', 'senha', 'confirmar_senha']

    def clean(self):
        cleaned_data = super().clean()
        return super().clean()