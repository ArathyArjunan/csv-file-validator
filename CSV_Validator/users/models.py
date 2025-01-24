from django.db import models

# Create your models here.


class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
