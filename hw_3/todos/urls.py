from django.urls import path
from .views import index_page, todo_detail, delete_things


urlpatterns = [
    path('', index_page),
    path('<int:pk>', todo_detail),
    path('<int:pk>/delete', delete_things)
]