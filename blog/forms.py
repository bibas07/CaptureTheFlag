from django import forms
from django.forms import ModelForm
from pyrsistent import field
from .models import ContactUsModel, SubscriptionModel, FlagModel


class SubscriptionForm(forms.ModelForm):

        class Meta:
            model = SubscriptionModel
            fields = ('subs_email',)
            labels = {
                'subs_email':'Your Email'
            }


class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUsModel
        fields = ('full_name', 'cont_email', 'address', 'message')
        labels = {
            'full_name': 'Full Name',
            'cont_email':'Email',
            'address':'Address',
            'message':'Message'
        }

class FlagForm(forms.ModelForm):

    class Meta:
        model = FlagModel
        fields = ("flag",)


