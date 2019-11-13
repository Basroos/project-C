from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout


urlpatterns =[
    path('',views.indexView,name="home_page"),
    path('login2/',LoginView.as_view(), name="login"),
    path('register2/',views.register,name="register"),
    path('logout2/',LogoutView.as_view(), name="logout")
]