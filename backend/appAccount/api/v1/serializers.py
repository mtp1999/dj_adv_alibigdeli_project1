from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAccount.models import User, Profile
from rest_framework.validators import ValidationError
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import gettext_lazy as _
from typing import Any, Dict


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise ValidationError({"detail": "Passwords are not the same!!"})

        try:
            validate_password(attrs.get('password'))
        except ValidationError as e:
            raise ValidationError({"Password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return User.objects.create_user(**validated_data)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_verified:
                raise serializers.ValidationError({"detail": "user is not verified!"})
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        if not self.user.is_verified:
            raise serializers.ValidationError({"detail": "user is not verified!"})
        data['email'] = self.user.email
        data['id'] = self.user.id

        return data


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, data):

        if data.get('new_password') != data.get('new_password1'):
            raise ValidationError({"detail": "Passwords are not the same!!"})

        try:
            validate_password(data.get('new_password'))
        except ValidationError as e:
            raise ValidationError({"Password": list(e.messages)})
        return super().validate(data)


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ["user", "email", "username", "first_name", "last_name", "birth_date", "image", "description"]
        read_only_fields = ["user", "email"]


class ActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        try:
            user_object = User.objects.get(email=attrs.get("email"))
        except User.DoesNotExist:
            raise ValidationError(
                {"detail": "User does not exist!"}
            )
        if user_object.is_verified:
            raise ValidationError(
                {"detail": "User is already verified!"}
            )
        attrs["user"] = user_object
        return super().validate(attrs)
