#Url for Blog routing
#name is used  to DRY urls in the html files
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]