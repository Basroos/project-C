from django import forms
from farmer_page.models import Farmer

class UpdateUser(forms.ModelForm):
    # email = forms.EmailField(
    #         max_length=40)
    name = forms.CharField(max_length=60)
    farm = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=10)
    address = forms.CharField(
        max_length=10)
    age = forms.CharField(
    max_length=2, required=False)
    province = forms.CharField(
        max_length=50)
    products = forms.CharField(
        max_length=50)

    class Meta:
        model = Farmer
        # email
        fields = ('name', 'age', 'farm', 'address', 'province', 'phone_number', 'products')

