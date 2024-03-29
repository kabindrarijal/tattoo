from django.db import models

class Tatto(models.Model):
    title       = models.CharField(max_length=120)
    description =models.TextField(blank=True, null=True)
    price       =models.DecimalField(decimal_places=2,max_digits=100000)
    category    = models.CharField(max_length=120)# max length is required
    features    =models.BooleanField(default=True)