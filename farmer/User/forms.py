from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    #username = forms.CharField(max_length=40, help_text='Enter a username')
    email = forms.EmailField(max_length=40, help_text='Enter a valid email adress')
    name = forms.CharField(max_length=60, required=False, help_text='Enter your full name')
    farm = forms.CharField(max_length=30, required=False, help_text='Enter the name of your farm/company')
    phone_number = forms.CharField(max_length=10,help_text='enter a valid phone number')
    address = forms.CharField(
        max_length=10, help_text='enter a valid address')
    age = forms.CharField(
    max_length=2, help_text='enter your age')
    province = forms.CharField(
        max_length=50, help_text='enter your province')
    products = forms.CharField(
        max_length=50, help_text='which products do you expect to sell')

    class Meta:
        model = User
        fields = ('username', 'name', 'age', 'farm', 'address', 'province','email', 'phone_number', 'products','password1', 'password2')
