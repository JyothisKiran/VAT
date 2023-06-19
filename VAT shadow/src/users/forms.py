from typing import Any, Dict
from django.forms import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    model = User
    fields = ['email', 'password']
    
