from django.db import models

from apps.customers.models import Customers
from apps.services.models import Services
from apps.employes.models import Employes
from apps.coordinators.models import Coordinators


# Create your models here.

class Bookings(models.Model):
    booking_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employes, on_delete=models.CASCADE)
    coordinators = models.ForeignKey(Coordinators, on_delete=models.CASCADE)