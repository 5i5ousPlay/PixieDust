from django.db import models
from product.models import Product
# Create your models here.


class Inventory(models.Model):
    COLOR_CHOICES = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('PURPLE', 'Purple'),
        ('PINK', 'Pink'),
        ('BLACK', 'Black')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    color = models.CharField(max_length=25)
    stock = models.IntegerField(default=0)
