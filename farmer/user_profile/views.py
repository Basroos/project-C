from django.shortcuts import render

# Create your views here.

def user_profile(request):
    template_name = 'user_profile/user_profile.html'
    return render(request, template_name)

def add_product(request):
    template_name = 'user_profile/add_product.html'
    return render(request, template_name)