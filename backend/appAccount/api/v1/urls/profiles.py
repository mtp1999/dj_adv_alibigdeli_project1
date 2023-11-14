from django.urls import path
from .. import views

urlpatterns = [

    # user profile
    path('', views.ProfileAPIView.as_view(), name='profile'),
]