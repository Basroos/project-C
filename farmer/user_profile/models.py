from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1)


    def __int__(self):
        #return "Farmer " + self.product_user.username + "\tProduct " + self.product_name
        return self.id
    

    
    def get_add_to_cart_url(self):
        print('1')
        return reverse("product_cart:add-to-cart", kwargs={
        "id": self.id
        })

    def get_remove_from_cart_url(self):
        print('1')
        return reverse("product_cart:remove-from-cart", kwargs={
        "id": self.id
        })

    product_picture = models.ImageField(blank=True, upload_to='images/')


class productReview(models.Model):
    review_title = models.CharField(max_length=30)
    review_message = models.CharField(max_length=200)
    review_product = models.IntegerField()

    def __str__(self):
        return "Product " + str(self.review_product) + "\ttitle " + self.review_title    