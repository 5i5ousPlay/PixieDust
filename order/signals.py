from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import OrderItem, Order


@receiver(post_save, sender=OrderItem)
def get_orderitem_total(sender, instance, created, *args, **kwargs):
    if created:
        instance.total = (instance.product.price * instance.quantity) * (1-instance.discount)
        instance.save()


# @receiver(post_save, sender=Order)
# def get_order_recepient(sender, instance, created, *args, **kwargs):
#     if created:
#         if instance.gift == False:
#             instance.recepient