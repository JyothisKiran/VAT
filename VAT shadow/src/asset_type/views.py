from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import AssetType
# Create your views here.

class AssettypeListView(ListView):
    model = AssetType
    template_name = 'asset_type/list.html'


class AssettypeAddView(CreateView):
    model = AssetType
    fields = ['type_name','description']
    template_name = 'asset_type/add.html'
    