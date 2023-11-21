from django.db import models
from order.models import Order
# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=255)


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='transaction', null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, related_name='transaction', null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='transaction', null=True)
