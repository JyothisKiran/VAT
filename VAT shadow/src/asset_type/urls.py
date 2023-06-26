from django.urls import path
from .views import AssettypeListView,AssettypeAddView,AssettypeUpdateView,AssettypeDetailView,AssettypeDeleteView

urlpatterns = [
    path('list/',AssettypeListView.as_view(),name='list'),
    path('add/',AssettypeAddView.as_view(),name='add'),
    path('update/<int:pk>/',AssettypeUpdateView.as_view(),name='update'),
    path('detail/<int:pk>/',AssettypeDetailView.as_view(),name='detail'),
    path('delete/<int:pk>/',AssettypeDeleteView.as_view(),name='delete'),
]