from django.urls import path

from .views import UserLoginSucessView, UserLoginView, ForgotPasswordView

urlpatterns = [
    path('success/', UserLoginSucessView.as_view(), name='success'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('forgotpw/', ForgotPasswordView.as_view(), name='forgotpw')
]
