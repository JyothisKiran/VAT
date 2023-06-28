from django.urls import path
from .views import UploadAssetView

urlpatterns = [
    path('add/',UploadAssetView.as_view(),name='upload'),
]