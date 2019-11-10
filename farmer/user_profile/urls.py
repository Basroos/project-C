from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user-profile'),
    path('add_product/', views.post_product, name='add-product')
]

