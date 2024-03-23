from django.urls import path
from .views import index_page,todo_details, delete_things

urlpatterns = [
    path('', index_page),
    path('/<int:pk>/details', todo_details),
    path('/<int:pk>/delete', delete_things)
]