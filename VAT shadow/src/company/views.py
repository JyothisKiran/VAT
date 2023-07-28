from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


class CompanyListView(ListView):
    model = Company
    template_name = 'company/list.html'


class CompanyAddView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/add.html'

    success_url = reverse_lazy('list-company')

    def form_valid(self, form):
        company_name = form.cleaned_data['company_name']
        company_code = form.cleaned_data['company_code']
        contact_person = form.cleaned_data['contact_person']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        print(company_code)
        obj = Company.objects.filter(company_code=company_code)
        print(obj)
        if not obj.exists():
            Company.objects.create(
                company_name=company_name,
                company_code=company_code,
                contact_person=contact_person,
                phone_number=phone_number,
                email=email
            )
            data = {'success': True}
            return JsonResponse(data=data)
        else:
            data = {'success': False}
            return JsonResponse(data=data, safe=False)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/detail.html'
    context_object_name = 'company'


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/update.html'
