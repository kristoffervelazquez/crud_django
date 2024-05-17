# companies/urls.py
from django.urls import path
from .views import index, add_company, edit_company, delete_company

app_name = 'companies'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_company, name='add_company'),
    path('edit/<int:pk>/', edit_company, name='edit_company'),
    path('delete/<int:pk>/', delete_company, name='delete_company'),
]
