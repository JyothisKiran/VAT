from typing import Any
from django.forms.models import BaseModelForm

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from .forms import AssettypeCreateForm
from .models import AssetType

# Create your views here.


class AssettypeListView(ListView):
    model = AssetType
    template_name = 'asset_type/list.html'
    context_object_name = 'asset'


class AssettypeCreateView(CreateView):
    model = AssetType
    template_name = 'asset_type/add.html'
    form_class = AssettypeCreateForm

    def form_valid(self, form):
        typename = form.cleaned_data['type_name']
        if AssetType.objects.filter(type_name=typename).exists():
            print('exists')
            data = {'fail': True}
            return JsonResponse(data)
        else:
            print('valid')
            self.object = form.save(commit=False)
            self.object.asset_type = typename  # Make the asset_type field required
            if typename:
                self.object.save()
                data = {'success': True}
                return JsonResponse(data)
            else:
                data = {'success': False}
                return JsonResponse(data, safe=False)

    def form_invalid(self, form):
        return JsonResponse(form.errors.as_json(), safe=False)


class AssettypeUpdateView(UpdateView):
    model = AssetType
    fields = ['type_name', 'description']
    template_name = 'asset_type/update.html'

    def form_valid(self, form):
        print('valid')
        typename = form.cleaned_data['type_name']
        asset_id = AssetType.objects.get(type_name=typename)
        if AssetType.objects.filter(type_name=typename).exists() and self.get_object():
            print('exists')
            data = {'success': False, 'id': asset_id.id}
            return JsonResponse(data, safe=False)
        else:
            form.save(commit=True)
            data = {'success': True}
            return JsonResponse(data, safe=False)

    def form_invalid(self, form):
        print('invalid')
        return JsonResponse(form.errors.as_json(), safe=False)


class AssettypeDetailView(DetailView):
    model = AssetType
    template_name = 'asset_type/detail.html'
    context_object_name = 'asset'


class AssettypeDeleteView(DeleteView):
    model = AssetType
    template_name = 'asset_type/delete.html'
    context_object_name = 'asset'
    success_url = reverse_lazy('list')