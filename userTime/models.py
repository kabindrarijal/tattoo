from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.db import models,IntegrityError
from django.contrib.auth import get_user_model

class UserTime(models.Model):
    username=models.CharField(blank=True,null=True,max_length=300)
   # phone=models.CharField(blank=True,null=True,max_length=20)
    time = models.TimeField(blank=True,null=True )
    date = models.DateField(blank=True,null=True)
