from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

# Create your views here.

def indexView(request):
    return render(request, 'home.html')

def LogoutView(request):
    return render(request,'logout_url')
    
@login_required
def LoginView(request):
    return render(request,'home.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')  
    else:
            form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})

