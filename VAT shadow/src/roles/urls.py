from django.urls import path
from .views import AddRoleView

urlpatterns = [path('add/', AddRoleView.as_view(), name='role_add')]
