from django.urls import path
from .views import SignupView, signup_page, VerifyOTP, LoginView, login_page,verify_otp_page,dashboard_page

urlpatterns = [
    # HTML pages
    path('signup-page/', signup_page, name='signup_page'),
    path('login-page/', login_page, name='login_page'),
    path('dashboard/',dashboard_page,name='dashboard'),

    # API endpoints
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify_otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-page/', verify_otp_page, name='verify_page'),
]