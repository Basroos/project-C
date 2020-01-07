from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from user_profile.models import Product
from product_cart.models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


@login_required(login_url='/login/login')
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
    if iqty + order_item.quantity > order_item.item.stock:
        return redirect("cartView")
    else:
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
        
    
@login_required(login_url='/login/login')
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
        return redirect("cartView")
    


def checkout(request):
    try:
        o = Order.objects.get(user=request.user, ordered=False)
        oi = OrderItem.objects.filter(user=request.user, ordered=False)
        o.ordered = True
        oi.update(ordered=True)
        o.save()
    except:
        return redirect("cartView")

    # stockUpdate = OrderItem.objects.filter(user=request.user, ordered=True)
    # item = get_object_or_404(Product, id=id)

    # updatedStock = stockUpdate.stock - stockUpdate.quantity
    # stockUpdate.item.stock = updatedStock
    # supdate.save()

    template = 'checkout/checkout.html'
    return render(request, template)

@login_required(login_url='/login/login')
def cartView(request):
    orderQS = Order.objects.filter(user=request.user, ordered=False)
    if orderQS.exists():
        pass
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, orderedDate=ordered_date)
        #messages.info(request,"this item was added to your cart")



    cart = Order.objects.get(user=request.user, ordered=False)
    context = {
        "cart": cart,
    }
    template = "cart/cartview.html"
    return render(request, template, context)


def OHistory(request):
    OH = Order.objects.filter(user=request.user, ordered=True)

    context = {
        "OH": OH,
    }
    template = "orderhistory/OHistory.html"
    return render(request, template, context)


def orderInfo(request, id):
    OI = Order.objects.filter(user=request.user, ordered=True, id=id)
    OIC = Order.objects.get(user=request.user, ordered=True, id=id)

    context = {
        "OI": OI,
        "OIC": OIC,
    }
    template = "orderhistory/orderInfo.html"
    return render(request, template, context)