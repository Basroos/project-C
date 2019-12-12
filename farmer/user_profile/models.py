from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

CHOICES = (
    (1, 'poor'),
    (2, 'below average'),
    (3, 'average'),
    (4, 'above average'),
    (5, 'good')
)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()


    def __str__(self):
        return "Farmer " + self.product_user.username + "\tProduct " + self.product_name
    

    
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

    def __str__(self):
        return "Farmer " + self.product_user.username + "\tProduct " + self.product_name

class Review(models.Model):
    name = models.CharField(max_length=20)
    grade = models.IntegerField(choices=CHOICES)
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Farmer " + self.product_user.username + "\tProduct " + self.product_name
