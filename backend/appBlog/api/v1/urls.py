from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = 'appBlog-api-v1'

# urlpatterns = [
#     path('posts/', views.PostList.as_view(), name='post_list'),
#     path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
#
#     path('blog/category/<str:category>/', views.BlogView.as_view(), name='blog_category'),
#     path('blog/tag/<str:tag>/', views.BlogView.as_view(), name='blog_tag'),
#     path('blog/author/<str:author>/', views.BlogView.as_view(), name='blog_author'),
#     path('blog/<int:pid>/', views.SingleView.as_view(), name='single'),
#
#     path('posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
#     path('posts/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
#                                                        'delete': 'destroy'}), name='post_detail'),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
urlpatterns = router.urls
