from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name ='blog-home'),#it maps to home view from view.py => def home
    path('post/<int:pk>',PostDetailView.as_view(), name ='post-detail'),
    path('about/',views.about, name= 'blog-about'),
    
]
