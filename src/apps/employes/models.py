from django.db import models

# Create your models here.

class Employes(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    number_file = models.IntegerField()
    state = models.BooleanField(default=True)