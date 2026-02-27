from .models import Machine
from django.forms import ModelForm, TextInput, Textarea

class MachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = ['m_name', 'machine_type', 'status', 'full_text']

        widgets = {
            'm_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название станка'
                                       }),
            'machine_type': TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип станка'
                                       }),
            'status': TextInput(attrs={'class': 'form-control', 'placeholder': 'Статус'
                                       }),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'
                                       }),
        }
