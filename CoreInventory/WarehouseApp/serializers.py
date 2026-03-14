from rest_framework import serializers
from .models import Warehouse
from LocationApp.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'state', 'pincode']


class WarehouseSerializer(serializers.ModelSerializer):
    location_details = LocationSerializer(source='location', read_only=True)

    class Meta:
        model = Warehouse
        fields = ['w_id', 'w_name', 'w_location', 'location', 'location_details']