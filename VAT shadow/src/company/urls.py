from django.urls import path
from .views import CompanyAddView, CompanyListView, CompanyDetailView, CompanyUpdateView

urlpatterns = [
    path('add/', CompanyAddView.as_view(), name='add-company'),
    path('list/', CompanyListView.as_view(), name='list-company'),
    path('detail/<int:pk>/', CompanyDetailView.as_view(), name='detail-company'),
    path('update/<int:pk>/', CompanyUpdateView.as_view(), name='update-company'),
]