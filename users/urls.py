"""hats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('singup/', users_views.signUp, name='signup'),
    path('profile/', users_views.profile, name='profile'),
    path('info/', users_views.userInfo, name="userinfo"),
]
