from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
from django.views import generic

# Create your views here.


class CompanyListView(generic.ListView):
    model = Company
    template_name = 'company/list.html'


class CompanyAddView(generic.CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/add.html'
