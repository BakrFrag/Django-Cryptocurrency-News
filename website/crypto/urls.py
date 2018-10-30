from django.contrib import admin
from django.urls import path;
from . import views;
urlpatterns = [
    path('',views.home,name="home"),
    path('news',views.news,name="news"),
    path('prices',views.prices_page,name="prices"),
    path('about',views.about,name="about"),
]
