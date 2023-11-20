from django.db import models
from django.db.models import Sum
from product.models import Product
# Create your models here.


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    delivery_address = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    amount_due = models.FloatField(default=0)
    gift = models.BooleanField(default=False)
    recepient = models.CharField(max_length=255, blank=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderitem')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem')
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)