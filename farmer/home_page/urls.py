from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('login/', views.login_index, name='login_index')
]
