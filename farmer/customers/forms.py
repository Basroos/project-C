from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#custom user sign up fields for farmers
class SignUpForm(UserCreationForm):
    #username = forms.CharField(max_length=40, help_text='Enter a username')
    email = forms.EmailField(max_length=40, help_text='Enter a valid email adress')
    name = forms.CharField(max_length=60, required=False, help_text='Enter your full name')
    address = forms.CharField(max_length=10, help_text='enter a valid address')
    
    class Meta:
        model = User
        fields = ('username', 'name', 'address','email', 'password1', 'paswword2')