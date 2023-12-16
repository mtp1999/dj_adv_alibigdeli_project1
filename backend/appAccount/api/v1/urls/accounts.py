from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    # registration
    path("registration/", views.RegistrationAPIView.as_view(), name="registration"),
    # change password
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change-password"
    ),
    # auth token
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.DeleteAuthTokenAPIView.as_view(), name="token-logout"),
    # jwt
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    # send test email
    path("email/", views.SendTestEmail.as_view(), name="send_test_email"),
    # activation
    path(
        "activation/<str:token>/", views.ActivationAPIView.as_view(), name="activation"
    ),
    path(
        "activation/resend/email/",
        views.ActivationResendGenericAPIView.as_view(),
        name="activation-resend",
    ),
]
