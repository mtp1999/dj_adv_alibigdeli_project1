from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateAPIView,
    get_object_or_404,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from appAccount.models import User, Profile
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ActivationResendSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .utils import SendEmailThread
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings


class SendTestEmail(APIView):
    def get(self, request, format=None):
        try:
            self.email = "admin2.admin2@gmail.com"
            user_object = get_object_or_404(User, email=self.email)
            token = self.get_tokens_for_user(user_object)
            message = EmailMessage(
                "email/test.tpl",
                {"token": token},
                "from@example.com",
                ["to@example.com"],
                subject="account activation",
            )
            thread = SendEmailThread(message)
            thread.start()

            return Response({"detail": "email sent!!"})
        except Http404:
            return Response({"detail": "account does not exist!!"})
        except:
            return Response({"detail": "Errorrrr!!!!"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}

            user_object = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_object)
            message = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "from@example.com",
                ["to@example.com"],
                subject="account activation",
            )
            thread = SendEmailThread(message)
            thread.start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivationResendGenericAPIView(GenericAPIView):
    serializer_class = ActivationResendSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        token = self.get_tokens_for_user(serializer.validated_data["user"])
        message = EmailMessage(
            "email/activation_email.tpl",
            {"token": token},
            "sender@example.com",
            [serializer.validated_data["email"]],
            subject="account activation",
        )
        thread = SendEmailThread(message)
        thread.start()
        return Response(
            {"detail": "Verification email sent! Please check your email."},
            status=status.HTTP_200_OK,
        )


class ActivationAPIView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response(
                {"detail": "Token is expired!"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.DecodeError:
            return Response(
                {"detail": "Token is invalid!"}, status=status.HTTP_400_BAD_REQUEST
            )
        user_id = token.get("user_id")
        user_object = get_object_or_404(User, id=user_id)
        if user_object.is_verified:
            return Response(
                {"detail": "User is already verified!"}, status=status.HTTP_200_OK
            )
        user_object.is_verified = True
        user_object.save()
        return Response(
            {"detail": "User verified successfully!"}, status=status.HTTP_200_OK
        )


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class DeleteAuthTokenAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(GenericAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
