from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.TopicTitlesView.as_view(), name = 'topic-titles'),
    path('<int:pk>/', views.ForumPosts.as_view(), name = 'title-posts'),
    path('create_title/', views.createTitle, name ='create-title'),
    path('<int:pk>/create_post', views.createPost, name = 'create-post'),
]
