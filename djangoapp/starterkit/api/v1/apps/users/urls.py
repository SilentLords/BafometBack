from django.urls import path, include
from .views import SendConfirmOtpToEmail,ConfirmEmailOTP, RegisteringNewUser, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('/auth/token/', TokenObtainPairView.as_view()),
    path('/auth/token/refresh', TokenRefreshView.as_view()),
    path('/auth/registrate/send_email/', SendConfirmOtpToEmail.as_view()),
    path('/auth/registrate/confirm_email/', ConfirmEmailOTP.as_view()),
    path('/auth/registrate/me/', RegisteringNewUser.as_view()),
    path('/auth/me/', UserView.as_view()),
]