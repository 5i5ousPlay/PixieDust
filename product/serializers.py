from rest_framework import serializers
from .models import Product, Folder, PenOrganizer, Planner
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    features = serializers.CharField()
    personalization = serializers.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                                      MaxValueValidator(limit_value=100)])
    price = serializers.FloatField(default=0, validators=[MinValueValidator(limit_value=0)])
    collection = serializers.CharField(max_length=1)
    length = serializers.FloatField(default=0, validators=[MinValueValidator(limit_value=0)])
    width = serializers.FloatField(default=0, validators=[MinValueValidator(limit_value=0)])
    height = serializers.FloatField(default=0, validators=[MinValueValidator(limit_value=0)])
    slots = serializers.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                            MaxValueValidator(limit_value=100)])

    def create(self, validated_data):
        collection = validated_data['collection']
        if collection == 'F':
            validated_data.pop('slots')
            folder = Folder.objects.create(**validated_data)
            return folder
        elif collection == 'O':
            validated_data.pop('length')
            validated_data.pop('width')
            validated_data.pop('height')
            po = PenOrganizer.objects.create(**validated_data)
            return po
        elif collection == 'P':
            validated_data.pop('slots')
            planner = Planner.objects.create(**validated_data)
            return planner
        else:
            raise ValidationError("Value is not a product type")


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 0, 'max_value': None},
            'personalization': {'min_value': 0, 'max_value': None},
            'length': {'min_value': 0, 'max_value': None},
            'width': {'min_value': 0, 'max_value': None},
            'height': {'min_value': 0, 'max_value': None}
        }


class PenOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenOrganizer
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 0, 'max_value': None},
            'personalization': {'min_value': 0, 'max_value': None},
            'slots': {'min_value': 0, 'max_value': None}
        }


class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 0, 'max_value': None},
            'personalization': {'min_value': 0, 'max_value': None},
            'length': {'min_value': 0, 'max_value': None},
            'width': {'min_value': 0, 'max_value': None},
            'height': {'min_value': 0, 'max_value': None}
        }


class ProductListSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        if isinstance(instance, Folder):
            return FolderSerializer(instance=instance).data
        elif isinstance(instance, PenOrganizer):
            return PenOrganizerSerializer(instance=instance).data
        elif isinstance(instance, Planner):
            return PlannerSerializer(instance=instance).data

    class Meta:
        model = Product
        fields ='__all__'
