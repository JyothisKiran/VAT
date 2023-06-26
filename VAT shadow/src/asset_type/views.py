from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import AssetType
from django.urls import reverse_lazy
# Create your views here.

class AssettypeListView(ListView):
    model = AssetType
    template_name = 'asset_type/list.html'


class AssettypeAddView(CreateView):
    model = AssetType
    fields = ['type_name','description']
    template_name = 'asset_type/add.html'

class AssettypeUpdateView(UpdateView):
    model = AssetType
    fields =['type_name','description']
    template_name = 'asset_type/update.html'
    success_url = reverse_lazy('list')

    
class AssettypeDetailView(DetailView):
    model= AssetType
    template_name = 'asset_type/detail.html'
    context_object_name = 'asset'

class AssettypeDeleteView(DeleteView):
    model = AssetType
    template_name = 'asset_type/delete.html'
    context_object_name = 'asset'
    success_url = reverse_lazy('list')