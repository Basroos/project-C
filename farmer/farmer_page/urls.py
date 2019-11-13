from django.urls import path
from . import views

urlpatterns = [
    path('',views.farmer_index, name='farmer-index'),
    path('profile/<id>', views.profile, name='profile-index'),
    path('search/', views.search_farmer, name='farmer-search'),
    path('my_products/',views.my_products, name='my-products')
]