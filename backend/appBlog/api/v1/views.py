from rest_framework.permissions import IsAuthenticated
from appBlog.models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PostList(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticated]


class PostDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticated]

