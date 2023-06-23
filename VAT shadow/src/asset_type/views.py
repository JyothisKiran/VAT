from django.shortcuts import render
from django.views.generic import ListView
from .models import AssetType
# Create your views here.

class AssettypeListView(ListView):
    model = AssetType
    template_name = 'asset_type/list.html'
    