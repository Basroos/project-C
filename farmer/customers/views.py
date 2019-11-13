from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from User.forms import SignUpForm
from django.contrib.auth.hashers import make_password

# Create your views here (Functions or classes.)

def indexView(request):
    return render(request, 'home.html')

def LogoutView(request):
    return render(request,'logout')

@login_required
def LoginView(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            raw_pass = make_password(form.cleaned_data.get('password1'))
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            #user = user.set_password(password1)
           # login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/reg.html',{'form':form})