from rest_framework import serializers
from .models import OrderItem, Order
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from django.db.models import Sum


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'discount', 'quantity', 'total']
        read_only_fields = ['total', 'order']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True)
    transaction = TransactionSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['amount_due']

    def create(self, validated_data):
        transaction_data = validated_data.pop("transaction")
        ag_trans = Transaction.objects.create(**transaction_data)
        item_data = validated_data.pop("orderitem")
        order = Order.objects.create(**validated_data)
        for item_data in item_data:
            item = OrderItem.objects.create(**item_data)
            item.order = order
            item.save()
            print(item)
        order.amount_due = order.orderitem.all().aggregate(Sum("total"))["total__sum"]
        order.save()
        ag_trans.order = order
        ag_trans.save()
        if order.gift == False:
            order.recepient = ag_trans.customer.name
            order.save()
        return order
