from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewPosts

# Initialize the router
router = DefaultRouter()
router.register('posts', ViewPosts, basename='post')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
