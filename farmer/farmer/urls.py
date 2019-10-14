from django.contrib import admin
from django.urls import path, include 

from profile_page.views import profile_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('farmer/', include('farmer_page.urls')),
    path('profile/', include('user_profile.urls')),
    path('login/', include('User.urls')),
]
