from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from User.forms import SignUpForm
from User.forms import SignUpForm2
from django.contrib.auth.hashers import make_password
from farmer_page.models import Farmer

# Create your views here (Functions or classes.)

def indexView(request):
    return render(request, 'home.html')

def LogoutView(request):
    return render(request,'logout_url')

@login_required
def LoginView(request):
    return render(request,'home.html')

def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            fullname= form.cleaned_data.get('name')
            raw_pass = form.cleaned_data.get('password1')
            raw_pass = make_password(form.cleaned_data.get('password1'))
            email = form.cleaned_data.get('email')
            farm = form.cleaned_data.get('farm')
            address = form.cleaned_data.get('address')
            age = form.cleaned_data.get('age')
            province = form.cleaned_data.get('province')
            phone = form.cleaned_data.get('phone_number')
            products = form.cleaned_data.get('products')
            farmer = Farmer(name=username, fullname=fullname, address=address, age=age,
            province=province, company_name=farm, phone_number=phone, products=products, email=email)
            farmer.save()
            #user = user.set_password(password1)
           # login(request, user)
            return redirect('login_url')
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html',{'form':form})

def customerView(request):
    if request.method == 'POST':
        form = SignUpForm2(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            raw_pass = make_password(form.cleaned_data.get('password1'))
            email = form.cleaned_data.get('email')
            #name = form.cleaned_data.get('name')
            #user = user.set_password(password1)
            #login(request, user)
            return redirect('login_url')
    else:
        form = SignUpForm2()

    return render(request, 'registration/reg.html',{'form':form})
