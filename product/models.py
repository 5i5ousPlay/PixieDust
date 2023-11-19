from django.db import models
from model_utils.managers import InheritanceManager

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



