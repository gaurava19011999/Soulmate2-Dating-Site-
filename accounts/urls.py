from django.urls import path

from . import views

urlpatterns = [
    path('register', views.Signup, name='sign_up'),
    path('login', views.Login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.Profile, name='profile'),
    # path('home', views.Home, name='home'),
]