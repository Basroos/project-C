from django.forms import ModelForm
from django import forms
from user_profile.models import Product, productReview
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user', None)
         super(ProductForm, self).__init__(*args, **kwargs)

    # product_name = forms.CharField(max_length=150, required=True)
    # product_description = forms.CharField(max_length=300, required=True)
    # product_price = forms.DecimalField(max_digits=6, decimal_places=2)
    # product_picture = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_price','product_picture')

class ReviewForm(forms.ModelForm):
    review_title = forms.CharField(max_length=30)
    review_message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), max_length=200)

    class Meta:
        model = productReview
        fields = ('review_title', 'review_message')