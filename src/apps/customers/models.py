from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

