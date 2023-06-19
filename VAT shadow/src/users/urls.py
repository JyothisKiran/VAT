from .views import UserLoginSucessView
from .views import UserLoginView
from django.urls import path

urlpatterns = [
    path('success/',UserLoginSucessView.as_view(),name ='success'),
    path('login/',UserLoginView.as_view(),name ='login'),
]
