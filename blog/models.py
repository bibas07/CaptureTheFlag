from django.db import models
# Create your models here.

class SubscriptionModel(models.Model):
    subs_email = models.CharField(max_length=100)

class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=50)
    cont_email = models.EmailField()
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

class FlagModel(models.Model):
    flag = models.CharField(max_length=100)

    def __str__(self):
        return self.flag