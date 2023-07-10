from django.db import models
from products.models import Products

class Expense(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    expensedate = models.DateField()
