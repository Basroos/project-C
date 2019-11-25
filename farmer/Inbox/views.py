from django.shortcuts import render, redirect

# Create your views here.
def indexView(request):
    return render(request, 'home.html')

def InboxView(request):
    return render(request, 'inbox.html')



