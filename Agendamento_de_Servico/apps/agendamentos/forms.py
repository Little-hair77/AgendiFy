from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Agendamento
        fields = ['data_hora', 'observacoes']  # só esses!

        widgets = {
            'data_hora': forms.DateTimeInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'type': 'datetime-local'
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'rows': 4,
                'placeholder': 'Observações adicionais'
            }),
        }

        labels = {
            'data_hora': 'Data e Hora',
            'observacoes': 'Observações',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.initial['data_hora'] = self.instance.data_hora.strftime('%Y-%m-%dT%H:%M')
