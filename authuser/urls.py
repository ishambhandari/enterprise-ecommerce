from django.contrib import admin
from django.urls import path,include
from .views import UserRegistrationView, login_view, logout_view

urlpatterns = [
    path('register_page/', UserRegistrationView.as_view(), name='register'),
    path('login/', login_view, name = 'login'),
    path('login_page/', login_view, name = 'login_page'),
    path('logout/', logout_view, name = 'logout'),
]
