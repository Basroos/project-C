from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from User.forms import SignUpForm

# Create your views here.

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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})
    

