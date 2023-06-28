from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AssetDataUploadForm
from .models import AssetData

# Create your views here.

class UploadAssetView(CreateView):
    model = AssetData
    template_name = 'upload_asset/add.html'
    form_class = AssetDataUploadForm
