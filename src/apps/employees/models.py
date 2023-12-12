from django.db import models
from django.contrib.auth.models import User

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    number_file = models.IntegerField()
    state = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.last_name}, {self.name}"
