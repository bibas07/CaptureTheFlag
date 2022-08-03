from django import forms
from requests import request
from .models import Profile, UserInfo
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user_profile']
        labels = {
            'user_profile':'Image path'
        }

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','email']
        labels = {
            'first_name': 'First Name',
            'last_name':'Last Name',
            'email':'Email',
            
        }