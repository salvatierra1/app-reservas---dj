from django.db import models

# Create your models here.

class Coordinators(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    dni = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)
    
=======
    name = models.CharField(max_length=50)
>>>>>>> 353df4daa0fe43bd6a5823ddc9cd81c637d70669
