from django.db import models
from model_utils.managers import CompositeField
from model_utils.managers import InheritanceManager


class Name(CompositeField):
    First = models.CharField(max_length=255)
    Last = models.CharField(max_length=255)


class SalesAgent(models.Model):
    Name = Name()


class Customer(models.Model):
    Name = Name()