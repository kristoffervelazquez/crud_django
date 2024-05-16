# models.py
from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='unknown')
    image = models.ImageField(upload_to='contacts/', null=True, blank=True)

    def __str__(self):
        return self.name
