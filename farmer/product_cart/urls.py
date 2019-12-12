from django.urls import path
from . import views


urlpatterns = [
    path('add_to_cart/<id>/', product_cart.views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.cartView, name='cartView'),
]
