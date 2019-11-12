from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

try:
    class SignUpForm(UserCreationForm):
        #username = forms.CharField(max_length=40, help_text='Enter a username')
        email = forms.EmailField(max_length=40, help_text='Enter a valid email adress')
        name = forms.CharField(max_length=60, required=False, help_text='Enter your full name')
        farm = forms.CharField(max_length=30, required=False, help_text='Enter the name of your farm/company')
        phone_number = forms.CharField(max_length=10, help_text='enter a valid phone number')
        adress = forms.CharField(max_length=10, help_text='enter a existing adress')



        class Meta:#asdasd
            model = User
            fields = ('username', 'name', 'farm', 'email', 'phone_number', 'password1', 'password2')
except:
    pass