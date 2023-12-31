from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('contrib/', include('contrib.urls')),
    path('asset/', include('asset_type.urls')),
    path('uploadasset/', include('upload_asset.urls')),
    path('roles/', include('roles.urls')),
    path('company/', include('company.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
