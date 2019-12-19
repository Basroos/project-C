from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_picture = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return "Farmer " + self.product_user.username + "\tProduct " + self.product_name

class productReview(models.Model):
    grade = models.IntegerField(choices=CHOICES)
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "Product " + self.review_product.product_name + "\tgrade " + str(self.grade)
