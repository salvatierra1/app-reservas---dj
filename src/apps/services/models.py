from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    state = models.BooleanField(default=True)