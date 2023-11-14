from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'appAccount'

urlpatterns = [
    path('login/', views.LogInView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/v1/', include('appAccount.api.v1.urls')),
    path('api/v2/', include('djoser.urls')),
    path('api/v2/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)