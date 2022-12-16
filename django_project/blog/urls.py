from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='blog-home'),#it maps to home view from view.py => def home
]
