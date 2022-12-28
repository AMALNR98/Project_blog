from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name ='blog-home'),#it maps to home view from view.py => def home
    path('about/',views.about, name= 'blog-about'),
]
