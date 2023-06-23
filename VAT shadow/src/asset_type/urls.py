from django.urls import path
from .views import AssettypeListView

urlpatterns = [
    path('list/',AssettypeListView.as_view(),name='list'),
]