from django.urls import path
from .views import register, otp_verification, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('otp-verification/<str:username>/<str:mobile_number>/', otp_verification, name='otp_verification'),
    path('dashboard/', dashboard, name='dashboard'),
]
