from django.db import models
from user_profile.models import Product
from django.conf import settings
from django.contrib.auth.models import User


from farmer_page.models import Farmer




class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    orderItemCode = models.IntegerField(default=0)

    def __int__(self):
        return self.item.product_name

    def getSubTotal(self):
        return self.quantity * self.item.product_price

    def getTotal(self):
        total = 0
        for Order_item in OrderItem.objects.all():
            total += Order_item.getSubTotal()
        return total    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    creationDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField()



    def __str__(self):
        return self.user.username

    def getTotal(self):
        total = 0
        for Order_item in self.items.all():
            total += Order_item.getSubTotal()
        return total
