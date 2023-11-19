from django.db import models
from model_utils.managers import CompositeField
from model_utils.managers import InheritanceManager
from rest_framework import generics


class OrderItem(models.Model):
    Quantity = models.IntegerField(default=0)
    objects = InheritanceManager()


class DeliveryAddress(CompositeField):
    Street = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    City = models.CharField(max_length=255)


class Order(models.Model):
    DateOrdered = models.DateField()
    DeliverySchedule = models. DateTimeField()
    DeliveryAddress = DeliveryAddress()
    GIFT_CHOICES = [
        ("Y", "Yes"),
        ("N", "No")
    ]
    #amount due
    

class Yes(Order):
    IntendedReciepient = models.CharField(max_length=255)


class No(Order):
   AuthorizedReciepient = models.CharField(nax_length=255)
