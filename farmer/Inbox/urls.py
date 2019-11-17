from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout


urlpatterns =[
    path('',views.indexView,name="home_page"),
    

   