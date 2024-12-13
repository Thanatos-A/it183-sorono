from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import viewPosts

# Initialize the router
router = DefaultRouter()
router.register('posts', viewPosts, basename='post')