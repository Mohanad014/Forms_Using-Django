from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome, name= 'Welcome'),
    path('home/',views.home, name= 'Home'),
]

