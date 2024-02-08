from django.contrib import admin
from django.urls import path
from .views import get_index_page, get_films_details



urlpatterns = [
    path('movies', get_index_page),
    path('movies/<int:pk>', get_films_details)
]