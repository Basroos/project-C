from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from user_profile.models import Product
from product_cart.models import order, orderItem
from django.contrib import messages
from django.db.models import Sum



def add_to_cart(request, id):
    try:
        qty = request.GET.get('qty')
    except:
        qty = 1

    item = get_object_or_404(Product, id=id)
    order_item, created = orderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    orderQS = order.objects.filter(user=request.user, ordered=False)
    if orderQS.exists():
        order = orderQS[0]
        if order.products.filter(item__slug=Product.slug).exists():
            order_item.quantity += qty
            order_item.save()
            messages.info(request,"this item quantity was updated")
            return redirect("product_cart:cartView")
        else:
            messages.info(request,"this item was added to your cart")
            order.items.add(order_item)
            return redirect("product_cart:cartView")
    else:
        ordered_date = timezone.now()
        order = order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"this item was added to your cart")
        return redirect("product_cart:cartView")



def remove_from_cart(request, id):
    print('1')
    item = get_object_or_404(Product, id=id)
    orderQS = order.objects.filter(
        user=request.user,
        ordered=False
    )
    print('1')
    if orderQS.exists():
        order = orderQS[0]
        print('1')
        if order.products.filter(item__id=Product.id).exists():
            order_item, created = orderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            print('1')
            return redirect("product_cart:cartView")
        else:
            return redirect("product_cart:cartView")
            print('1')
    else:
        return redirect("product_cart:cartView")
        print('1')
    


def checkout():
    #update stock in database with ordered quantity
    #move to new page
    template = 'checkout/checkout.html'
    return render(request, template)


def cartView(request):
    cart = orderItem.objects.all()
    #totalPrice = 0
    #for item in cart:
    #    totalPrice += orderItem.quantity * item.item.product_price
    context = {
        "cart": cart,
        #"total":totalPrice
    }
    template = "cart/cartview.html"
    return render(request, template, context)