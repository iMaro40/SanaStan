from django.contrib.auth.models import User
from django.urls import path
from userprofile import views
urlpatterns = [
    path('', views.myprofile, name = 'profile')
]
