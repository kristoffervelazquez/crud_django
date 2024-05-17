# events/urls.py
from django.urls import path
from .views import index, add_event, edit_event, delete_event

app_name = 'events'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_event, name='add_event'),
    path('edit/<int:pk>/', edit_event, name='edit_event'),
    path('delete/<int:pk>/', delete_event, name='delete_event'),
]
