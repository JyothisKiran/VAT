from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import UserLoginForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = UserLoginForm
    next_page = 'success'

    def form_valid(self, form: UserLoginForm) -> HttpResponse:
        email = form.cleaned_data('email')
        password = form.cleaned_data('password')
        user = authenticate(username =email,password=password)

        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
        else:
            form.add_error("Invalid credentials. Please enter the correct details.")
            return super().form_invalid(form)

    
class UserLoginSucessView(TemplateView):
    template_name = 'users/success.html'