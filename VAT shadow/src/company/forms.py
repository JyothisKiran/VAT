from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter company name'}))
    company_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter company code'}))
    contact_person = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter contact person name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))

    class Meta:
        model = Company
        fields = ['company_name', 'company_code', 'contact_person', 'phone_number', 'email']
