import datetime

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone
from .models import *

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.CharField()

    class Meta:#conf in single place
        model =User
        fields=['username','email','phone','password1']





