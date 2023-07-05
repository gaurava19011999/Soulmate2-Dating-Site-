from django.urls import path

from . import views

urlpatterns = [
    path('<str:room>/', views.room, name='room'),
    path('<str:room2>/', views.room2, name='room2'),
    path('default', views.default, name='default'),
    path('check/<str:data>/view', views.check, name='check'),
    path('send', views.send, name='send'),
    path('send2', views.send2, name='send2'),
    path('test', views.test, name='test'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getMessages2/<str:room>/', views.getMessages2, name='getMessages2'),
]