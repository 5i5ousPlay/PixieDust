from django.db import models
from model_utils.managers import InheritanceManager
from model_utils.managers import CompositeField
# Create your models here.


class Product(models.Model):
    COLLECTION_CHOICES = [
        ("F", "Folder"),
        ("O", "Pen Organizer"),
        ("P", "Planner")
    ]
    name = models.CharField(max_length=255)
    features = models.TextField(blank=True)
    personalization = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    collection = models.CharField(max_length=1, choices=COLLECTION_CHOICES)
    objects = InheritanceManager()


class Folder(Product):
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)


class PenOrganizer(Product):
    slots = models.IntegerField(default=0)


class Planner(Product):
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)


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


#class No(Order):
   #multivariable authorized recipient


class Name(CompositeField):
    First = models.CharField(max_length=255)
    Last = models.CharField(max_length=255)


class SalesAgent(models.Model):
    Name = Name()


class Customer(models.Model):
    Name = Name()