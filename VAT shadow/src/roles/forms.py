from django import forms
from .models import Role


class RoleAddForm(forms.ModelForm):
    ROLE_CHOICES = (( 'Admin', 'Admin'), ( 'Auditor', 'Auditor'))
    role_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type role name'}), max_length=100)
    role_type = forms.ChoiceField(widget=forms.RadioSelect, choices=ROLE_CHOICES)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type description',}), max_length=200)

    class Meta:
        model = Role
        fields = ['role_name', 'role_type', 'description']
