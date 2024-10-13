# users/urls.py
from django.urls import path
from .views import register, profile_view, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
