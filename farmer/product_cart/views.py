from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from user_profile.models import Product
from product_cart.models import order, orderItem
from django.contrib import messages
from django.db.models import Sum



def add_to_cart(request, id):
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
            #add custom quantity to add to cart
            order_item.quantity += 1
            order_item.save()
            messages.info(request,"this item quantity was updated")
            return redirect("product_cart:product",id=id)
        else:
            messages.info(request,"this item was added to your cart")
            order.items.add(order_item)
            return redirect("product_cart:product",id=id)
    else:
        ordered_date = timezone.now()
        order = order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"this item was added to your cart")
        return redirect("product_cart:product",id=id)



def remove_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    orderQS = order.objects.filter(
        user=request.user,
        ordered=False
    )
    if orderQS.exists():
        order = orderQS[0]
        if order.products.filter(item__id=Product.id).exists():
            order_item, created = orderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request,"this item was removed from your cart")
            return redirect("product_cart:product",id=id)
        else:
            messages.info(request,"this item was not in your cart")
            return redirect("product_cart:product",id=id)
    else:
        messages.info(request,"you do not have an order yet")
        return redirect("product_cart:product",id=id)
    


def checkout():
    #update stock in database with ordered quantity
    #move to new page
    return render(request, checkout.html)


def cartView(request):
    cart = orderItem.objects.all()
    context = {
        "cart": cart,
    }
    template = "cart/cartview.html"
    return render(request, template, context)