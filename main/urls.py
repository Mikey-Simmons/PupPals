from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('signup', views.registration),
    path('login',views.login),
    path('register', views.register),
    path('welcome', views.welcome),
    path('logout', views.logout)
]