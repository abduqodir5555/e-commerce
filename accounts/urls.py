from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from accounts.views import *


urlpatterns = [
    path("register/", UserCreateView.as_view(), name='register'),
    path("verify-otp/", VerifyOtpView.as_view(), name="verify-otp"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/start/', PasswordResetStartView.as_view(), name='password_reset_start'),
    path('password-reset/finish/', PasswordResetFinishView.as_view(), name='password_reset_finish')
]

