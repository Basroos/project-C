from django.contrib import admin
from django.urls import path, include 

from profile_page.views import profile_index
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('farmer/', include('farmer_page.urls')),
    path('profile/', include('user_profile.urls')),
    path('login/', include('User.urls')),
    path('inbox/', include('Inbox.urls')),
    path('products/', include('user_profile.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
