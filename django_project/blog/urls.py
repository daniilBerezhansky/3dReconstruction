from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('reconstruction/', views.Reconstruction.as_view(), name='reconstruction'),
    path('posts/', views.Posts.as_view(), name='posts'),
]
