from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_info(models.Model):
  
    userName = models.OneToOneField(User, null = False, unique=True, on_delete = models.CASCADE)
    tell = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address  = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.email
  
    