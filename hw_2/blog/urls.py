from django.contrib import admin
from django.urls import path
from .views import get_article_details, get_article_index_page



urlpatterns = [
    path('articles', get_article_index_page),
    path('articles/<int:pk>', get_article_details)
]