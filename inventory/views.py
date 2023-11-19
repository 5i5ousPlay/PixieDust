import django_filters
from django.shortcuts import render
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class InventoryCreateView(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryListFilterSet(FilterSet):
    color = django_filters.CharFilter(method='filter_color')
    product = django_filters.NumberFilter(method='filter_product')

    def filter_color(self, queryset, name, value):
        color = value
        if color is not None:
            queryset = queryset.filter(color=color)
        return queryset

    def filter_product(self, queryset, name, value):
        product_id = value
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventoryListFilterSet


class InventoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = 'id'
