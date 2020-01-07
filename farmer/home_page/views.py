from django.shortcuts import render
from django.http import HttpResponse
from farmer_page.models import Farmer
from user_profile.models import Product
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.

def home_index(request):
    return render(request, 'home_page/home.html', {'navigation':'home', 'info':Farmer.objects.all()})

def login_index(request):
    return render(request, 'login_page/login.html')

def quick_product(request, prodname):
    template_name = "user_profile/product.html"
    # product.delete(pk=id)
    
    product = Product.objects.filter(product_name=prodname).values()
    if len(product) < 1:
      messages.info(request, 'Product not available.')
      return redirect('home_index')
    else:
      return render(request, template_name, {"quick_product": product})

def guidelines(request):
    return render(request, 'home_page/userguidelines.html')