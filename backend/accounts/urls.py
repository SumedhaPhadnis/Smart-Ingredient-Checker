from django.urls import path

# Combine both branches so we keep ALL the views!
from .views import (
    EmailTokenObtainPairView,
    VerifyEmailAPIView,
    CookieTokenRefreshView,
    LogoutAPIView,
    MeAPIView,
    RegisterAPIView,
    GoogleLoginAPIView,
    AdditiveListAPIView,  # Kept from your feature branch
    ResendOTPAPIView,     # Kept from main branch
)

urlpatterns = [
    path("register/",          RegisterAPIView.as_view(),          name="register"),
    path("token/",           EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('verify-email/<uuid:token>/', VerifyEmailAPIView.as_view(), name='verify-email'),
    path("token/refresh/",   CookieTokenRefreshView.as_view(), name="token_refresh"),
    # Keep going with the rest of your paths below this...
]
