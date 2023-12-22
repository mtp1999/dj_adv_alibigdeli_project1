from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from appBlog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PostListPagination
from .filters import PostListFilter


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # filterset_fields = ['categories', 'author']
    filterset_class = PostListFilter
    search_fields = ["title", "categories__name"]
    ordering_fields = ["published_date"]
    pagination_class = PostListPagination


class PostListRenderTemplate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "appBlog/blog.html"

    def get(self, request, **kwargs):
        posts = Post.objects.filter(status=1).order_by("-published_date")
        if s := request.GET.get("search"):
            posts = posts.filter(title__contains=s)
        if a := kwargs.get("author"):
            posts = posts.filter(author__username=a)
        if c := kwargs.get("category"):
            posts = posts.filter(categories__name=c)
        if t := kwargs.get("tag"):
            posts = posts.filter(tags__name__icontains=t)

        posts = Paginator(posts, 3)
        page_number = request.GET.get("page", 1)
        # try:
        posts = posts.page(page_number)
        # except PageNotAnInteger:
        #     return redirect("appBlog:post_list")
        # except EmptyPage:
        #     return redirect("appBlog:post_list")

        return Response({'posts': posts})
