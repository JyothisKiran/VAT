# from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AssetDataUploadForm
from .models import AssetData

# Create your views here.


class UploadassetAdd(CreateView):
    model = AssetData
    template_name = 'upload_asset/add.html'
    form_class = AssetDataUploadForm
    success_url = reverse_lazy('list')

    def form_valid(self, form: form_class) -> HttpResponse:
        print('valid')
        return super().form_valid(form)

    def form_invalid(self, form: form_class) -> HttpResponse:
        print('invalid')
        return super().form_invalid(form)


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
