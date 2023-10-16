from rest_framework import serializers
from appBlog.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'status', 'published_date']

