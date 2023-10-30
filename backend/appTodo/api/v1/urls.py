from . import views
from rest_framework import routers

app_name = 'api-v1'


router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet, basename='jobs')
urlpatterns = router.urls
