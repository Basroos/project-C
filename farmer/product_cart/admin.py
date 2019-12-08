from django.contrib import admin
from product_cart.models import order
from product_cart.models import orderItem

admin.site.register(order)
admin.site.register(orderItem)
