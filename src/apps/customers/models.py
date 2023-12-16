from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.last_name}, {self.name}"
