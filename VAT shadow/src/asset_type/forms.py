from django import forms

from .models import AssetType


class AssettypeCreateForm(forms.ModelForm):
    type_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter type name',
            'id': "id_type_name",
            'name': "type_name",
        }),
        max_length=150,
        required=False
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter description',
                'id': 'id_description',
                'name': 'description',
            }
        ),
        max_length=250,
        required=False
    )

    class Meta:
        model = AssetType
        fields = ['type_name', 'description']
