from django.shortcuts import render
from user_profile.forms import ProductForm
from user_profile.models import Product
# Create your views here.

def user_profile(request):
    template_name = 'user_profile/user_profile.html'
    return render(request, template_name)

def add_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    return render(request, template_name, {'form': form})

def post_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    if request.method == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['product_name']
            description = form.cleaned_data['product_description']
            price = form.cleaned_data['product_price']
            user = request.user
            product = Product(name, description, price, user)
            product.save()
            return render(request, 'home_page/home.html', {'product': product})
        else:
            form = ProductForm() #baba
    return render(request, template_name, {'form':form})
