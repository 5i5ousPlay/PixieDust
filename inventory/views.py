from django.shortcuts import render
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
# Create your views here.


class InventoryCreateView(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
