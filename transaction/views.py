from django.shortcuts import render
from rest_framework import generics
from .serializers import TransactionSerializer
from .models import Transaction
# Create your views here.


class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
