from django.urls import path
from .views import AssettypeListView,AssettypeAddView

urlpatterns = [
    path('list/',AssettypeListView.as_view(),name='list'),
    path('add/',AssettypeAddView.as_view(),name='add'),
]