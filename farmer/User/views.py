from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
def indexView(request):
    return render(request, 'home.html')

@login_required
<<<<<<< Updated upstream
def LoginView(request):
    return render(request,'home.html')
=======
def dashboardView(request):
    return render(request,'farmer.html')
>>>>>>> Stashed changes

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< Updated upstream
            return redirect('login_url')  
    else:
            form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})
=======
            return redirect('home_page/home.html')  
    else:
            form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})
>>>>>>> Stashed changes
