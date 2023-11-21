from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import OrderItem, Order
from inventory.models import Inventory
from django.db.models import Sum


@receiver(post_save, sender=OrderItem)
def get_orderitem_total(sender, instance, created, *args, **kwargs):
    if created:
        instance.total = (instance.product.price * instance.quantity) * (1-instance.discount)
        instance.save()


@receiver(post_save, sender=OrderItem)
def decrement_inventory(sender, instance, created, *args, **kwargs):
    if created:
        color = instance.color
        product = instance.product
        quantity = instance.quantity
        inventory = Inventory.objects.get(product=product, color=color)
        inventory.stock -= quantity
        inventory.save()
