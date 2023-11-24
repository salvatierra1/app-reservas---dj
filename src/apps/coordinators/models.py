from django.db import models

# Create your models here.

class Coordinators(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    dni = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)
