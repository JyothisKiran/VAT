from typing import Any, Dict

from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms

from .models import User


class UserLoginForm(AuthenticationForm):
    model = User
    fields = '__all__'
    
