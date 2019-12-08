from django.forms import ModelForm
from django import forms
from user_profile.models import Product
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user', None)
         super(ProductForm, self).__init__(*args, **kwargs)

    product_name = forms.CharField(max_length=150, required=True)
    product_description = forms.CharField(max_length=300, required=True)
    product_price = forms.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_price')