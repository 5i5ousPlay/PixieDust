from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'agent', 'order', 'date', 'total']
        read_only_fields = ['order']

    def get_date(self, obj):
        if obj.order:
            return obj.order.date
        else:
            return None

    def get_total(self, obj):
        if obj.order:
            return obj.order.amount_due
        else:
            return None
