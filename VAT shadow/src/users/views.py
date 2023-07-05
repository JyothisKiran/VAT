from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import UserLoginForm


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = UserLoginForm
    next_page = 'success'

    def form_valid(self, form: UserLoginForm) -> HttpResponse:
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username =email,password=password)

        if user is not None:
            login(self.request,user)
            return JsonResponse({'success': True})
        else:
            form.add_error("Invalid credentials. Please enter the correct details.")
            return JsonResponse({'success': False, 'message': 'Invalid login credentials.'})


    
class UserLoginSucessView(TemplateView):
    template_name = 'users/success.html'