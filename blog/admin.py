from django.contrib import admin
from .models import ContactUsModel, FlagModel

# Register your models here.

admin.site.register(ContactUsModel)
admin.site.register(FlagModel)