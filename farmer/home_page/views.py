from django.shortcuts import render
from django.http import HttpResponse
from farmer_page.models import Farmer
# Create your views here.

def home_index(request):
    return render(request, 'home_page/home.html', {'navigation':'home', 'info':Farmer.objects.all()})

def login_index(request):
    return render(request, 'login_page/login.html')

def guidelines(request):
    return render(request, 'home_page/userguidelines.html')