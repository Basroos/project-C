from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('login/', views.login_index, name='login_index'),
    path("logout/", LogoutView.as_view(), name="logout_url"),
]

