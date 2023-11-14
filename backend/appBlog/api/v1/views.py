from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from appBlog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PostListPagination
from .filters import PostListFilter


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['categories', 'author']
    filterset_class = PostListFilter
    search_fields = ['title', 'categories__name']
    ordering_fields = ['published_date']
    pagination_class = PostListPagination




