from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser,Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserRegisteratoinForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','stage','permissions']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']