
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
from .models import UserTime

class user_form(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(
    ),initial=timezone.now())
    date = forms.DateField(initial=datetime.now())


    class Meta:

        model=UserTime
        fields=['time','date']