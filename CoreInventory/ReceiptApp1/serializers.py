from rest_framework import serializers
from .models import Receipt
from WarehouseApp.models import Warehouse


class ReceiptSerializer(serializers.ModelSerializer):

    warehouse_name = serializers.CharField(source='reference.w_name', read_only=True)

    class Meta:
        model = Receipt
        fields = [
            'id',
            'reference',
            'warehouse_name',
            'from_location',
            'to_location',
            'contact',
            'schedule_date',
            'status'
        ]