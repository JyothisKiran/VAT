from django.urls import path

from .views import (UploadassetAdd, UploadassetDetailView, UploadassetEditView,
                    UploadassetList)

urlpatterns = [
    path('add/', UploadassetAdd.as_view(), name='assetdataupload'),
    path('list/', UploadassetList.as_view(), name='assetdatalist'),
    path('edit/<int:pk>/', UploadassetEditView.as_view(), name='assetdataedit'),
    path('detail/<int:pk>/', UploadassetDetailView.as_view(), name='assetdatadetail'),
]