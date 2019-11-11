from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email adress')
    name = forms.CharField(max_length=60, required=False, help_text='Enter your first name')
    farm = forms.CharField(max_length=30, required=False, help_text='Enter your last name')
    phone_number = forms.CharField(max_length=32, help_text='enter a valid phone number')


    class Meta:
        model = User
        fields = ('name','farm', 'email', 'phone_number', 'password1', 'password2')