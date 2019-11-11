from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_index(request):
    return render(request, 'home_page/home.html', {'navigation':'home'})

def login_index(request):
    return render(request, 'login_page/login.html')
