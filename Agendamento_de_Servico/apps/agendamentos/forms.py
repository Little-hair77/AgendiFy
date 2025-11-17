from django import forms
from models import Agendamento

class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Agendamento
        fields = ['empresa', 'servico', 'data_hora', 'observacoes', 'status']
        widgets = {
            'empresa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'servico': forms.Select(attrs={
                'class': 'form-control'
            }),
            'data_hora': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observações adicionais'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'empresa': 'Empresa',
            'servico': 'Serviço',
            'data_hora': 'Data e Hora',
            'observacoes': 'Observações',
            'status': 'Status do Agendamento'
        }

    def __init__(self):
        super().__init__(*args, **kwargs)

        # Ajusta o formato do campo data_hora para exibição no form
        if self.instance and self.instance.pk:
            self.initial['data_hora'] = self.instance.data_hora.strftime('%Y-%m-%dT%H:%M')