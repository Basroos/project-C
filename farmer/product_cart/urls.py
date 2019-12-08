from django.urls import path
from .views import add_to_cart, cartView


urlpatterns = [
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<id>/', add_to_cart, name='remove-from-cart'),
    path('cart/', cartView, name='cartView'),
]
