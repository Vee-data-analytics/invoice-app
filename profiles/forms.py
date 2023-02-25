from cProfile import label
from django import forms
from .models import Profiles
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = (
            'company_name', 
            'company_address', 
            'account_number', 
            'bank_name', 
            'company_reg_no',
            'vat_no',
            'company_logo'
        )

        label = {
            'company_name':'Company name',
            'company_address':'Address',
            'bank_name':'Bank Name',
            'account_number':'Account no.',
            'vat_no':'VAT number',
            'company_reg_no':'Registration no.',
            'company_logo':'Logo'
            
        }


    def clean_name(self):
        user_name = self.cleaned_data.get('company_name')
        if len(user_name) < 3:
            raise ValidationError('Name is too short')
        return user_name
