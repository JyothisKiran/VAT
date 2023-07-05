from django.urls import path

from .views import (AssettypeCreateView, AssettypeDeleteView,
                    AssettypeDetailView, AssettypeListView,
                    AssettypeUpdateView)

urlpatterns = [
    path('list/', AssettypeListView.as_view(), name='assetlist'),
    path('add/', AssettypeCreateView.as_view(), name='assetadd'),
    path('update/<int:pk>/', AssettypeUpdateView.as_view(), name='assetupdate'),
    path('detail/<int:pk>/', AssettypeDetailView.as_view(), name='assetdetail'),
    path('delete/<int:pk>/', AssettypeDeleteView.as_view(), name='assetdelete'),
]