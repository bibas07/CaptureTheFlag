from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from fastapi import FastAPI
from prometheus_client import generate_latest
from .models import Profile, UserInfo
from .forms import ProfileForm, UserInfoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# def signIn(request):
#     context = {
#         'title':'SignIn - NetworkHats'
#     }

# def signIn(request):
#     context = {
#         'title':'SignIn - NetworkHats'
#     }
#     if request.method == "POST":
#         login_form = AuthenticationForm(request=request, data=request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data.get("username")
#             password = login_form.cleaned_data.get("password")
#             user_login = authenticate(username=username, password=password)
#             login(request, user_login)
#             if username is not None:
#                 # payloads = ['"',"'","`",'or 1=1',"' or 1=1", 'or 1=1;',"'or 1=1;"]
#                 # while 'admin" or 1=1;--' or "' or 1=1;--" in username:
#                 #     admin_user = "anon"
#                 #     admin_pass = "bibas"
#                 #     user_login = authenticate(username=admin_user, password=admin_pass)
#                 #     login(request, user_login)
#                 #     messages.success(request, "You have successfully logged in as 'anon'. ")
#                 # else:
#                 #     for payload in payloads:
#                 #         if payload in username:
#                 #             messages.info(request, "Try hard. Try again. Try more.")
#                 # user_login = authenticate(username = username,password = password)
#                 # login(request, user_login)
#                 # messages.info(request, f"You are now logged in as {username}")
                
#                 if 'or 1=1;--' in login_form.username_field:
#                     user_admin = 'anon'
#                     user_password = 'bibas'
#                     login(request, (user_admin,user_password))
#                     messages.success(request,"You have successfully logged in as Anon")
#                     return redirect("dashboard")
#             return redirect("dashboard")
#     else:
#         login_form = AuthenticationForm()
#     context['login_form'] = login_form
#     return render(request, 'users/signin.html', context)

def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"You have successfully register ' {username} '. Please login ")
            form.save()
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request,'users/signup.html',{'form':form})

@login_required
class LogoutView(TemplateView):
    template_name = 'users/logout.html'

@login_required
def profile(request):
    context = {
        'title':'Profile',
        'user_images': Profile.objects.all(),
        'user_info': UserInfo.objects.all()
    }
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully uploaded profile picture')
            return redirect('profile')
        else:
            messages.warning(request, "Don't do this  --> Flag: NH{R3m0t3Fil3Inclu$i0n}")
            return redirect("profile")
    else:
        form = ProfileForm()
        context['form']= form
    return render(request, 'users/profile.html', context)

@login_required
def userInfo(request):
    context = {
        'title':'Your Information',
        'user_info':UserInfo.objects.all()
    }
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Your information have been saved')
            return redirect("profile")
    else:
        form = UserInfoForm()
        context['form'] = form
    return render(request, 'users/setup_info.html', context)