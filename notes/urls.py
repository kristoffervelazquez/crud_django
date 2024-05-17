# notes/urls.py
from django.urls import path
from .views import index, add_note, edit_note, delete_note

app_name = 'notes'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete_note'),
]
