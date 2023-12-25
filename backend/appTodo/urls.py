from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appTodo import views

app_name = "appTodo"

urlpatterns = [
    path("jobs/", views.JobsView.as_view(), name="jobs"),
    path("jobs/delete/<int:pk>/", views.JobDeleteView.as_view(), name="delete_job"),
    path("jobs/update/<int:pk>/", views.JobUpdateView.as_view(), name="update_job"),
    path("api/v1/", include("appTodo.api.v1.urls")),
    path("test_send_email/", views.test_send_email),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
