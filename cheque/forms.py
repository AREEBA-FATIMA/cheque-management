# forms.py
from django import forms
from .models import Cheque

class ChequeForm(forms.ModelForm):
    class Meta:
        model = Cheque
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'cheque_date': forms.DateInput(attrs={'type': 'date'}),
            'bill_available': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'shared_on_group': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        }

