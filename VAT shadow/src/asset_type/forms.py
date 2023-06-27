from django import forms
from .models import AssetType


class AssettypeCreateForm(forms.ModelForm):
    type_name = forms.CharField(max_length=255)
    description = forms.Textarea()

    class Meta:
        model = AssetType
        fields = '__all__'

