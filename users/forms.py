from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserRegisteratoinForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','stage']