from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomePage, name='Homepage'),
    path('', views.matching_system, name='matching'),
    path('friend_request/', views.send_friend_request, name='friend-request'),
    path('notify/', views.notification, name='notification'),
    path('notify/accept_friend_request/', views.accept_friend_request, name='accept-friend-request'),
    path('notify/decline_friend_request/', views.decline_friend_request, name='decline-friend-request'),

]