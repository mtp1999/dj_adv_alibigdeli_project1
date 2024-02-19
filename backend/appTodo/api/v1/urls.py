from django.urls import path

from . import views
from rest_framework import routers

app_name = "api-v1"

urlpatterns = [
    path('tehran_weather/', views.TehranWeatherAPIView.as_view())
]


router = routers.DefaultRouter()
router.register(r"jobs", views.JobViewSet, basename="jobs")
urlpatterns += router.urls
