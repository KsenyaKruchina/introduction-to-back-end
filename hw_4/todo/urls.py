from django.urls import path
from .views import things_page_view, todo_details_view, delete_things_page_view, index_page_view, edit_todo_view

urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('things/', things_page_view, name='things'),
    path('things/<int:pk>/details', todo_details_view, name='todo_details'),
    path('things/<int:pk>/delete', delete_things_page_view, name='delete_things_page'),
    path('things/<int:pk>/edit', edit_todo_view, name='edit_todo')
]
