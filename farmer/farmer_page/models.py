from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Farmer(models.Model):
    # naam, adres, leeftijd, provincie, email, bedrijfsnaam, telefoonnummer, producten
    name = models.CharField(max_length=60)
    fullname = models.CharField(max_length=44, default='ome henk', null=True)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, default="fbaba@gmail.com")
    age = models.CharField(max_length=2)
    province = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, default="farmer@farmer.nl")
    company_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    products = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class farmerReview(models.Model):
    review_title = models.CharField(max_length=30)
    review_message = models.CharField(max_length=200)
    review_farmer = models.IntegerField()

    def __str__(self):
        return "Farmer " + str(self.review_farmer) + "\ttitle " + self.review_title    