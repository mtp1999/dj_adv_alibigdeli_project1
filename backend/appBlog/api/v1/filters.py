import django_filters
from appBlog.models import Post


class PostListFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            "author": ["exact", "in"],
            "status": ["exact"],
        }
