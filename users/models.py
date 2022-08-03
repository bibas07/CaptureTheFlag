from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user_profile = models.ImageField(default='/user_profile/testimonal1.jpg', blank=False, upload_to='user_profile/')
    


class UserInfo(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name +" "+ self.last_name

    
    