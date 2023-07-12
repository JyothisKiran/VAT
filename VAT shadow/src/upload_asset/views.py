# from django.shortcuts import render
from django.forms.models import BaseModelForm
import pandas as pd
from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView

from .forms import AssetDataUploadForm
from .models import AssetData, DataModel

# Create your views here.


class AssetDataTemplateView(TemplateView):
    template_name = 'upload_asset/add.html'


class UploadassetAdd(CreateView):
    model = AssetData
    template_name = 'upload_asset/add.html'
    form_class = AssetDataUploadForm

    # def post(self, request, *args, **kwargs):

    #     instance = super().save(commit=False)

    #     # Get the uploaded file
    #     file = self.cleaned_data['file']

    #     # Read the Excel file using pandas
    #     df = pd.read_excel(file)

    #     # Process the data and store it in another model
    #     # Assuming you have another model called DataModel with fields: data_field1, data_field2
    #     for index, row in df.iterrows():
    #         data_model = DataModel(
    #             financial_year=row['FY (Financial Year)'],
    #             asset_owner=row['Asset Owner – Owned / Leased'],
    #             company_code=row['Company Code'],
    #             asset_class=row['Asset Class'],
    #             asset_class_descript=row['Asset Class Descript'],
    #             asset=row['Asset'],
    #             sub_no=row['Sub No.'],
    #             asset_description=row['Asset description'],
    #             manufacturer=row['Manufacturer'],
    #             type_name=row['Type Name'],
    #             serial_number=row['Serial Number'],
    #             department=row['Department'],
    #             personnel_number=row['Personnel Number'],
    #             name=row['Name'],
    #             sublocation=row['Sublocation'],
    #             leasing_company_code=row['Leasing company code'],
    #             leasing_company_name=row['Leasing company Name'],
    #             capitalization_date=row['Capitalization date'],
    #             plant=row['Plant'],
    #             acquisition_value=row['Acquisition value'],
    #             book_value=row['Book value'],
    #             high_value_flag=row['High Value Flag'],
    #             # Add other fields as required
    #         )
    #         data_model.save()

    #     if self.commit:
    #         instance.save()

    #     return instance
    # return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        file = form.cleaned_data['file']
        print('valid')
        if file is not None:
            form.save()
            print("\n\n dfee")
            data = {'success': True}
        else:
            data = {'success': False}
        return JsonResponse(data, safe=False)

    def form_invalid(self, form):
        return JsonResponse(form.errors.as_json(), safe=False)


class UploadassetList(ListView):
    model = AssetData
    template_name = 'upload_asset/list.html'


class UploadassetEditView(UpdateView):
    model = AssetData
    fields = '__all__'
    template_name = 'upload_asset/update.html'


class UploadassetDetailView(DetailView):
    model = AssetData
    # form_class = AssetDataUploadForm
    template_name = 'upload_asset/detail.html'
    context_object_name = 'assetdata'
