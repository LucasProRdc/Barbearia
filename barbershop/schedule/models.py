from django.db import models
from customers.models import Customers

class Schedule(models.Model):
    customer = models.ForeignKey(Customers, null=False, blank=False, on_delete=models.PROTECT)
    description = models.DateField(null=False, blank=False)
