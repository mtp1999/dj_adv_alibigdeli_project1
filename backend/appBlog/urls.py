from django.urls import path
from appBlog import views
from django.conf import settings
from django.conf.urls.static import static
from appBlog.feeds import LatestEntriesFeed
app_name = 'appBlog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/category/<str:category>/', views.BlogView.as_view(), name='blog_category'),
    path('blog/tag/<str:tag>/', views.BlogView.as_view(), name='blog_tag'),
    path('blog/author/<str:author>/', views.BlogView.as_view(), name='blog_author'),
    path('blog/<int:pid>/', views.SingleView.as_view(), name='single'),

    # path('contact/', views.contact_view, name='contact'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('rss/feed/', LatestEntriesFeed()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)