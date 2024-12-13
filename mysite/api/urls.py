from django.urls import path, include
from . import views
from . import api_url

urlpatterns = [
    path('', include(api_url)),
    path('add/', views.addPost),
    path('postdetail/<str:pk>/', views.viewPostDetail),
    path('update/<str:pk>/', views.updatePost),
    path('delete/<str:pk>/', views.deletePost),
]
