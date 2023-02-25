from cProfile import label
from django import forms
from .models import Client
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'name', 
            'website',
            'client_address', 
            'company_reg_no', 
            'vat_no', 
            'logo'
        )

        label = {
            'name: Name',
            'website: Website',
            'company_reg_no: Company Reg No',
            'vat_no: VAT Number',
            'logo: Campany logo',
            'client_address: Client info',
        }