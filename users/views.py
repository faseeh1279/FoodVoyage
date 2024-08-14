from django.shortcuts import render, redirect 
from django.contrib.auth import logout 
# Create your views here.

def login_view(request): 
    return render(request, 'users/login_page.html')


def signup_view(request): 
    return render(request, 'users/signup_page.html')


def home(request): 
    return render(request, "users/home.html")


def logout_view(request): 
    logout(request) 
    return redirect("/")