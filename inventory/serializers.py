from rest_framework import serializers
from rest_framework import validators
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Inventory.objects.all(),
                fields=['product','color']
            )
        ]
