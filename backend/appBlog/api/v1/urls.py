from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appBlog-api-v1'

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    # path('blog/category/<str:category>/', views.BlogView.as_view(), name='blog_category'),
    # path('blog/tag/<str:tag>/', views.BlogView.as_view(), name='blog_tag'),
    # path('blog/author/<str:author>/', views.BlogView.as_view(), name='blog_author'),
    # path('blog/<int:pid>/', views.SingleView.as_view(), name='single'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)