from django import forms
from .models import Estimate
from django.core.exceptions import ValidationError

class EstimateForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Completion date'  )
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Issue')
    
    class Meta:
        model = Estimate
        fields = (
            'clients', 
            'estimate_number', 
            'completion_date', 
            'issue_date',
        )

        label = {
            'estimate_number':'Quotation No.',
        }

    def clean_number(self):
        number = self.cleaned_data.get('estimate_number')
        if len(number) < 10:
            raise ValidationError('Number is too short')
        return number