from django.shortcuts import render
from user_profile.forms import ProductForm
from user_profile.models import Product
from profile_page.models import Farmer
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
# Create your views here.

def user_profile(request):
    template_name = 'user_profile/product.html'
    context = {'product':Product.objects.all()}
    return render(request, template_name, context)

def search_product(request):
    template = 'user_profile/product.html'
    query_product = request.GET.get("query")
    if query_product:
        result = Product.objects.filter(product_name__startswith=query_product)
        if len(result) < 1:
            empty = True
        else:
            empty = False
    return render(request, template, {"result":result, 'empty':empty})

def add_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    return render(request, template_name, {'form': form})

def post_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['product_name']
            description = form.cleaned_data['product_description']
            price = form.cleaned_data['product_price']
            user = request.user
            print(user)
            product = Product(product_name=name, product_description=description, product_price=price, product_user=user)
            product.save()
            return render(request, 'user_profile/product.html', {'product':Product.objects.all()})
        else:
            form = ProductForm()
    return render(request, template_name, {'form':form})
