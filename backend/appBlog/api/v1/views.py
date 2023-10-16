from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from appBlog.models import Post
from .serializers import PostSerializers


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, ])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        serializer = PostSerializers(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({'Detail': 'Post Deleted.'})


@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


