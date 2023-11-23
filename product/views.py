import django_filters
from django.shortcuts import render
from .models import Product
from .serializers import ProductCreateSerializer, ProductListSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.filterset import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class RegisterProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductSubclassMixin(object):
    def get_queryset(self):
        return Product.objects.select_subclasses()


class ProductListFilterSet(FilterSet):
    name = django_filters.CharFilter(method='filter_name')
    type = django_filters.CharFilter(method='filter_type')

    def filter_name(self, queryset, name, value):
        product_name = value
        if product_name is not None:
            queryset = queryset.filter(name__icontains=product_name)
        return queryset

    def filter_type(self, queryset, name, value):
        product_type = value
        if product_type is not None:
            queryset = queryset.filter(collection=product_type)
        return queryset


class ProductListView(ProductSubclassMixin, generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductListFilterSet


class ProductDetailView(ProductSubclassMixin, generics.RetrieveUpdateAPIView):
    serializer_class = ProductListSerializer
    lookup_field = 'id'


class ProductDeleteView(ProductSubclassMixin, generics.DestroyAPIView):
    serializer_class = ProductListSerializer
    lookup_field = 'id'

    def perform_destroy(self, instance):
        try:
            product_inventory = instance.inventory.all()
            for inventory in product_inventory:
                inventory.delete()
        except Exception as e:
            return Response(
                {"detail": str(e.args[0])}, status=status.HTTP_400_BAD_REQUEST
            )
