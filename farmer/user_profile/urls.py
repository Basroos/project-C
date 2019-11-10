from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user-profile'),
    path('add_product/', views.add_product, name='add-product')
]

