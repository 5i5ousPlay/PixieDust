from rest_framework import serializers
from .models import OrderItem, Order
from product.models import Product
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from django.db.models import Sum


class OrderItemSerializer(serializers.ModelSerializer):
    personalization = serializers.CharField(max_length=255, allow_blank=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'discount', 'quantity', 'total', 'color', 'personalization']
        read_only_fields = ['total', 'order']

    def validate_personalization(self, value):
        product_id = self.initial_data['product']
        product = Product.objects.get(id=product_id)
        product_personalization_limit = product.personalization
        if len(value) > product_personalization_limit:
            raise serializers.ValidationError("Personalization exceeds length limit")
        return value


class OrderListSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    agent = serializers.SerializerMethodField()
    orderitem = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'date', 'delivery_address', 'schedule', 'amount_due',
                  'gift', 'recepient', 'customer', 'agent', 'orderitem']

    def get_customer(self, obj):
        print(obj.transaction)
        if obj.transaction:
            return obj.transaction.customer.id
        else:
            return None

    def get_agent(self, obj):
        if obj.transaction:
            return obj.transaction.agent.id
        else:
            return None


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
