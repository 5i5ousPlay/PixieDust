from django.shortcuts import render
from .models import Product
from .serializers import ProductCreateSerializer, ProductListSerializer
from rest_framework import generics
# Create your views here.


class RegisterProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductSubclassMixin(object):
    def get_queryset(self):
        return Product.objects.select_subclasses()


class ProductListView(ProductSubclassMixin, generics.ListAPIView):
    serializer_class = ProductListSerializer
