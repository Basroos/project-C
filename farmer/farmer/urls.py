from django.contrib import admin
from django.urls import path, include 

from profile_page.views import profile_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',profile_index),
    path('',include('home_page.urls'))
]