from django.db import models


# Create your models here.
class Farmer(models.Model):
   First_Name = models.CharField(max_length=100, default="Boer Henk")
   Last_Name = models.CharField(max_length=100, default="Haroldsen")
   emailadress = models.EmailField(default="Email niet bekend")
   Address = models.CharField(max_length=100, default="Niet bekend")
   Farm_name = models.CharField(max_length=100, default="Farmerama")
   tel_nr = models.PositiveSmallIntegerField(default=0)

   def __str__(self):
      return '{} {} {} {} {}'.format(self.First_Name, self.Last_Name, self.emailadress, self.Address, self.Farm_name, self.tel_nr)
'''
class customer(models.Model):
   Name = models.CharField(max_length=100, default="Piet Klaasen")
   emailadress = models.EmailField(default="Email niet bekend")

   def __str__(self):
      return self.Name, self.emailaddress'''
   