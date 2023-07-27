from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import PrivilageMaster, Role
from .forms import RoleAddForm
from django.views.generic import CreateView

# Create your views here.


class AddRoleView(CreateView):
    model = Role
    template_name = 'roles/add.html'
    form_class = RoleAddForm

    def get_context_data(self, **kwargs):
        context = {}
        obj = PrivilageMaster.objects.all()
        context['obj'] = obj
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)