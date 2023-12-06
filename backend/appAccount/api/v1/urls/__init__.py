from django.urls import path, include

urlpatterns = [
    path("accounts/", include("appAccount.api.v1.urls.accounts")),
    path("profiles/", include("appAccount.api.v1.urls.profiles")),
]
