from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class UserDashboardView(TemplateView):
    template_name = 'contrib/base.html'