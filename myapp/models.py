from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
