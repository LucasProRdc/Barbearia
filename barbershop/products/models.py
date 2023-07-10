from django.db import models

class Products(models.Model):
    description = models.CharField(max_length=30, null=False, blank=False)
    #picture
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    category = models.CharField(max_length=30, null=False, blank=False)
    
