from django.db import models
from product.models import Product
# Create your models here.


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    delivery_address = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    amount_due = models.FloatField(default=0, null=True)
    gift = models.BooleanField(default=False)
    recepient = models.CharField(max_length=255, blank=True)


class OrderItem(models.Model):
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderitem')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem', null=True)
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    color = models.CharField(max_length=25, choices=COLOR_CHOICES)
    personalization = models.CharField(max_length=255, blank=True)
