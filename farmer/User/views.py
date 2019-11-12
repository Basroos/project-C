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
    return render(request,'logout_url')

@login_required
def LoginView(request):
    return render(request,'home.html')

def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Username')
            raw_pass = form.cleaned_data.get('password1')
            raw_pass = make_password(form.cleaned_data.get('password1'))
            #user = user.set_password(password1)
           # login(request, user)
            return redirect('login_url')
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html',{'form':form})



