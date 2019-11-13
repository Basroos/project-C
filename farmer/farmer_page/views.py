from django.shortcuts import render
from .models import Farmer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from farmer_page.models import Farmer
from django.db.models import Q
from user_profile.models import Product
# Create your views here.

def farmer_index(request):
    context = {'info': Farmer.objects.all(),
                'navigation':'farmer',}
    return render(request, 'farmer_page/farmer.html', context)


def profile(request, id):
    farmer = get_object_or_404(Farmer, pk=id)
    context = {'farmer':farmer}
    return render(request, 'farmer_page/profile.html', context)

def my_products(request):
    current_user = request.user.id
    template = 'farmer_page/my_products.html'
    profile = get_object_or_404(User, pk=current_user)
    # products = get_list_or_404(Product, product_user=request.user)
    products = Product.objects.filter(product_user=request.user)

    return render(request, template, {'profile':profile, 'product': products})


def search_farmer(request):
    template = 'farmer_page/farmer.html'
    query_farmer = request.GET.get("query")
    if query_farmer:
        # result = Farmer.objects.filter(Q(address__icontains=query_farmer) | Q(products__icontains=query_farmer))
        result = Farmer.objects.filter(name__startswith=query_farmer)
        if len(result) < 1:
            empty = True
        else:
            empty = False

    return render(request, template, {'result':result, 'empty':empty})
