from rest_framework import serializers
from appBlog.models import Post, Category
from appAccount.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.ReadOnlyField(source='get_absolute_api_url')
    absolute_url = serializers.SerializerMethodField()  # define a SerializerMethodField

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'status', 'snippet', 'categories', 'image', 'absolute_url', 'relative_url', 'published_date']
        read_only_fields = ['author', 'absolute_url']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.pk)
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('absolute_url', None)
            rep.pop('relative_url', None)

        rep['categories'] = CategorySerializer(instance.categories, many=True).data
        return rep



