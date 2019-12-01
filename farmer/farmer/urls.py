from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from profile_page.views import profile_index
import debug_toolbar
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('farmer/', include('farmer_page.urls')),
    path('profile/', include('user_profile.urls')),
    path('login/', include('User.urls')),
    path('products/', include('user_profile.urls')),
    path('__debug__/', include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
