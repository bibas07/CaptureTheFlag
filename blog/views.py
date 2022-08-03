from email import message
import imp
from re import sub
import re
from django.contrib import messages
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import SubscriptionForm, ContactUsForm, FlagForm
from .models import SubscriptionModel
# Create your views here.

"""
First interface where input form in below takes email address
then stores in a database
"""
def homePage(request):
    context = {
        'title':'Home',
        'subs_form':SubscriptionForm()
    }
    if request.method=="POST":
        subs_form = SubscriptionForm(request.POST)
        if subs_form.is_valid():
            subs_email = subs_form.cleaned_data.get('subs_email')
            messages.success(request,'You have successfully subscribed our newspaper by email:  '+subs_email)
            payloads = ["<scri","<h","<img","<ifra","<b","'",'"',"`" ]
            if '<script>alert(document.cookies)</script>' in subs_email:
                messages.success(request, "The flag is: NH{W0W_R3fl3ct3d_X$$}")
            else:
                for payload in payloads:
                    if payload in subs_email:
                        messages.info(request,"You are on the right path. Keep On Trying")
            
        return redirect("homepage")
    else:
        subs_form = SubscriptionForm()
    return render(request, 'blog/index.html', context)


def contactUsPage(request):
    context = {
        'title':'Contact Us',
        'contact_form':ContactUsForm
    }
    if request.method=="POST":
        subs_form = ContactUsForm(request.POST)
        if subs_form.is_valid():
            subs_form.save()
            con_address = subs_form.cleaned_data.get("address")
            messages.success(request,'Your message has been sent')
            payloads = ["<scri","<h","<img","<p","<ifra","<b","'",'"',"`" ]
            if (con_address.startswith("'<img src=") or con_address.startswith('"<img src=')) and con_address.endswith(">"):
                if 'onerror=alert(document.domain)' in con_address:
                    messages.success(request, "The flag is: NH{$t0r3d_X$$_I$_F0und3d}")
            else:
                for payload in payloads:
                    if payload in con_address:
                        messages.info(request,"You are on the right path. Keep On Trying")

        return redirect("contact-us")
    else:
        subs_form = ContactUsForm()
    return render(request, 'blog/contact_us.html', context)

# @login_required()
# def dashboard(request):
#     context = {
#         'title':'Dashboard',
#         'flag_form':FlagForm
#     }
#     list_ctf = ["NH{W0W_R3fl3ct3d_X$$}","NH{$t0r3d_X$$_I$_F0und3d}","NH{R3m0t3Fil3Inclu$i0n}","NH{Hidd3n_Fil3_F0und3d}","hello5"]
#     count = 0
#     flag_form = FlagForm(request.POST)
#     for ctf_ans in list_ctf:
#         if request.method == "POST":
#             flag_form = FlagForm(request.POST)
#             if flag_form.is_valid():
#                 submitted_flag = flag_form.cleaned_data.get("flag")
#                 if ctf_ans == submitted_flag:
#                     messages.success(request, "Congratulation! You have found flag")
#                     count += 12.5
#                     redirect("dashboard")         
#     else:
#         flag_form = FlagForm()
#         context['flag_percentage'] = count

#     return render(request, 'blog/dashboard.html', context)


@login_required()
def dashboard(request):
    context = {
        'title':'Dashboard',
        'flag_form':FlagForm
    }
    list_ctf = ["NH{W0W_R3fl3ct3d_X$$}","NH{$t0r3d_X$$_I$_F0und3d}","NH{R3m0t3Fil3Inclu$i0n}","NH{Hidd3n_Fil3_F0und3d}","NH{B@64_D3c0d3d}"]
    count = 0
    flag_form = FlagForm(request.POST)
    if request.method == "POST":
        flag_form = FlagForm(request.POST)
        if flag_form.is_valid():
            submitted_flag = flag_form.cleaned_data.get("flag")
            for ctf_ans in list_ctf:
                if ctf_ans == submitted_flag:
                    messages.success(request, "Congratulation! You have found flag")
                    count += 12.5
                    redirect("dashboard")   
            else:
                messages.warning(request, "Oops! Flag does not matched")      
    else:
        flag_form = FlagForm()
        context['flag_percentage'] = count

    return render(request, 'blog/dashboard.html', context)





def secret(request):
    context = {
        'title':'NetworkHats - CTF'
    }
    return render(request, 'blog/secret.html', context)

        