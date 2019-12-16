from django.db import models
from user_profile.models import Product
from django.conf import settings


#if user is the farmer
from farmer_page.models import Farmer




class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    #subTotal = models.DecimalField(max_digits=10000, decimal_places=2)


    def __int__(self):
        #return self.item.product_name
        return self.id
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    creationDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField()
    #total = models.DecimalField(max_digits=10000, decimal_places=2)
 


    def __str__(self):
        return self.user.username


