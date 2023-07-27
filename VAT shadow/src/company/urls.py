from django.urls import path
from .views import CompanyAddView, CompanyListView

urlpatterns = [
    path('add/', CompanyAddView.as_view(), name='add-company'),
    path('list/', CompanyListView.as_view(), name='list-company'),
]