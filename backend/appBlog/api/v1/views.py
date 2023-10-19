from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from appBlog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.filter(status=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, id=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=self.request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, id=pk)
        serializer = self.serializer_class(post, data=self.request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, id=pk)
        serializer = self.serializer_class(post, data=self.request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, id=pk)
        post.delete()
        return Response({'Detail': 'post deleted.'})



