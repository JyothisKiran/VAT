from django import forms
from .models import AssetData,DataModel
import pandas as pd
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')
class AssetDataUploadForm(forms.ModelForm):
    filename = forms.CharField(widget=forms.TextInput(attrs ={'placeholder':'Enter file name'}),max_length=50,required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs = {"placeholder": "Select date",
        # "id": "date_range_start",
        'type': 'date',
        'pattern': '\d{4}-\d{2}-\d{2}',
        'min': current_date,
        'onfocus': "this.showPicker()",
        'required': False}))
    end_date = forms.DateField(widget=forms.DateInput(attrs = {"placeholder": "Select date",
        # "id": "date_range_start",
        'type': 'date',
        'pattern': '\d{4}-\d{2}-\d{2}',
        'min': current_date,
        'onfocus': "this.showPicker()",
        'required': False}))
    file = forms.FileField(widget=forms.FileInput(attrs={'placeholder':'Select file'}))

    class Meta:#placeholder,id,type,pattern:'
        model = AssetData
        fields = ['filename','start_date','end_date','file']
        #fields = '__all__'
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Get the uploaded file
        file = self.cleaned_data['file']

        # Read the Excel file using pandas
        df = pd.read_excel(file)

        # Process the data and store it in another model
        # Assuming you have another model called DataModel with fields: data_field1, data_field2
        for index, row in df.iterrows():
            data_model = DataModel(
                financial_year = row['FY (Financial Year)'],
                asset_owner = row['Asset Owner – Owned / Leased'],
                company_code = row['Company Code'],
                asset_class = row['Asset Class'],
                asset_class_descript = row['Asset Class Descript'],
                asset = row['Asset'],
                sub_no = row['Sub No.'],
                asset_description = row['Asset description'],
                manufacturer = row['Manufacturer'],
                type_name = row['Type Name'],
                serial_number = row['Serial Number'],
                department = row['Department'],
                personnel_number = row['Personnel Number'],
                name = row['Name'],
                sublocation = row['Sublocation'],
                leasing_company_code=row['Leasing company code'],
                leasing_company_name=row['Leasing company Name'],
                capitalization_date=row['Capitalization date'],
                plant=row['Plant'],
                acquisition_value=row['Acquisition value'],
                book_value=row['Book value'],
                high_value_flag=row['High Value Flag'],
                # Add other fields as required
            )
            data_model.save()

        if commit:
            instance.save()

        return instance