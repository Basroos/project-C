from django.shortcuts import render, redirect
from user_profile.models import Product
from product_cart.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.


def indexView(request):
    return render(request, 'home.html')

def InboxView(request):
    return render(request, 'inbox.html')

def OHistory(request):
    OH = Order.objects.filter(user=request.user, ordered=True)
    
    context = {
        "OH": OH,
    }
    template = "OHistory.html"
    return render(request, template, context)


def orderInfo(request, id):
    OI = Order.objects.filter(user=request.user, ordered=True, id=id)
    OIC = Order.objects.get(user=request.user, ordered=True, id=id)
    
    context = {
        "OI": OI,
        "OIC": OIC,
    }
    template = "orderInfo.html"
    return render(request, template, context)
