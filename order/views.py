from django.shortcuts import render
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderCreateSerializer, OrderListSerializer
from rest_framework import generics

# Create your views here.


class OrderItemCreate(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
