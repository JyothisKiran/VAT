from datetime import datetime

import pandas as pd
from django import forms

from .models import AssetData, DataModel

current_date = datetime.now().strftime('%Y-%m-%d')


class AssetDataUploadForm(forms.ModelForm):
    filename = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter file name'}), max_length=50, required=False
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Select date",
                'type': 'date',
                'pattern': '\d{4}-\d{2}-\d{2}',
                'min': current_date,
                'onfocus': "this.showPicker()",
                'required': False
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Select date",
                'type': 'date',
                'pattern': '\d{4}-\d{2}-\d{2}',
                'min': current_date,
                'onfocus': "this.showPicker()",
                'required': False
            }
        )
    )
    file = forms.FileField(widget=forms.FileInput(attrs={'placeholder': 'Select file'}), required=False)

    class Meta:  # placeholder,id,type,pattern:'
        model = AssetData
        fields = ['filename', 'start_date', 'end_date', 'file']
        # fields = '__all__'
