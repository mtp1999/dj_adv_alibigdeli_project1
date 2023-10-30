from rest_framework import serializers
from appTodo.models import Job
from appAccount.models import Profile


class JobSerializer(serializers.ModelSerializer):

    relative_url = serializers.ReadOnlyField(source='get_absolute_api_url')
    absolute_url = serializers.SerializerMethodField()  # define a SerializerMethodField
    email = serializers.ReadOnlyField(source='return_email')  # define a SerializerMethodField

    class Meta:
        model = Job
        fields = ['id', 'absolute_url', 'relative_url', 'email', 'name', 'status', 'created_date', 'updated_date']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data['user'] = Profile.objects.get(user__id=self.context.get('request').user.pk)
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url', None)
            rep.pop('relative_url', None)
        return rep



