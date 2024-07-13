from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
    
class West_Info(models.Model):
    
 
    Image_Path = models.ImageField(upload_to = 'Images')
    Prediction = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add= True)
    Type = models.CharField(max_length=50)
    
    # userName = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
    # ID = models.CharField(max_length=100)
    # testType = models.CharField(max_length=100)
    # Address = models.CharField(max_length=100)
    # Date = models.DateTimeField(auto_now_add= True)
    # isPridicted = models.BooleanField(default=False)
    # WSImage = models.ImageField(upload_to = 'ws')
    
    def __str__(self):
        return self.Prediction
