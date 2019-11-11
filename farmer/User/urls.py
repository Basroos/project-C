from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout

urlpatterns =[
    path('',views.indexView,name="home_page"),
    path('login/',LoginView.as_view(), name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(), name="logout_url"),
    
]