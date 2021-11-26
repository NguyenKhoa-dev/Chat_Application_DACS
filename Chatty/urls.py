from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Chatty'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.UserLoginRegister, name='user'),
    path('logout/',views.logoutUser,name='logout'),
]