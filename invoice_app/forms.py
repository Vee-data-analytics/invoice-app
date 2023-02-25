from cProfile import label
from django import forms
from .models import Invoice
from django.core.exceptions import ValidationError

class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Completion date'  )
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Issue')
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Payment date')
    
    class Meta:
        model = Invoice
        fields = (
            'clients', 
            'invoice_number', 
            'completion_date', 
            'issue_date', 
            'payment_date'
        )

        label = {
            'invoice_number':'Invoice No.',
            'clients':'Client',
        }


'''

class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_number', 'name']'''