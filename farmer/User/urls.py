from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
<<<<<<< Updated upstream
    path('',views.indexView,name="home_page"),
    path('login/',LoginView.as_view(), name="login_url"),
    path('register/',views.registerView,name="register_url"),
=======
    path('',views.indexView,name="home_index"),
    path('login/',LoginView.as_view(), name="login_url"),
    path('register/',views.registerView, name="register_url"),
>>>>>>> Stashed changes
    path('logout/',LogoutView.as_view(next_page='logout'),name="logout"),
]