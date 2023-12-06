from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import User


class CostumeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    captcha = CaptchaField()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
