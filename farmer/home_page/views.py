from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def home_index(request):
    return render(request, 'home_page/home.html', {'navigation':'home'})

def login_index(request):
    return render(request, 'login_page/login.html')

def register_index(request):
    return render(request, 'register_page/register.html')
