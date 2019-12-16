from django.contrib import admin
from product_cart.models import Order
from product_cart.models import OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
