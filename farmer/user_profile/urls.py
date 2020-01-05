from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user-profile'),
    path('add_product/', views.post_product, name='add-product'),
    path('search/', views.search_product, name='product-search'),
    path('category/', views.category_products, name='category'),
    path('delete/<id>', views.delete_product, name='delete'),
    path('', views.review_product, name='save-review'),
]

