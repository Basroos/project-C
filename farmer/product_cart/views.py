from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from user_profile.models import Product
from product_cart.models import Order, OrderItem
from django.contrib import messages
from django.db.models import Sum



def add_to_cart(request, id):
    try:
        qty = request.GET.get('qty')
    except:
        qty = 1
    iqty = int(qty)

    item = get_object_or_404(Product, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    orderQS = Order.objects.filter(user=request.user, ordered=False)
    if orderQS.exists():
        order = orderQS[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += iqty
            order_item.save()
            messages.info(request,"this item quantity was updated")
            return redirect("cartView")
        else:
            messages.info(request,"this item was added to your cart")
            order.items.add(order_item)
            order_item.quantity = iqty
            order_item.save()
            return redirect("cartView")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, orderedDate=ordered_date)
        order.items.add(order_item)
        order_item.quantity = iqty
        order_item.save()
        messages.info(request,"this item was added to your cart")
        return redirect("cartView")
        
    # newSubTotal = 0.00
    # for item in OrderItem.objects.all():
    #     newSubTotal = item.quantity * item.product_price
    # orderItem.subTotal = newSubTotal    

    # newTotal = 0.00
    # for item in Order.items.all():
    #     newTotal += newSubTotal
    




def remove_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    orderQS = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if orderQS.exists():
        order = orderQS[0]
        order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        )
        order_item.delete()
        return redirect("cartView")
    else:
        pass
    


def checkout():
    #update stock in database with ordered quantity
    #move to new page
    template = 'checkout/checkout.html'
    return render(request, template)


def cartView(request):
    cart = OrderItem.objects.all()
    #totalPrice = 0
    #for item in cart:
    #    totalPrice += orderItem.quantity * item.item.product_price
    context = {
        "cart": cart,
        #"total":totalPrice
    }
    template = "cart/cartview.html"
    return render(request, template, context)