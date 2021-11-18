from rest_framework import serializers
from .models import L3


class L3Serializer(serializers.ModelSerializer):
    type_of_order = serializers.CharField(source='order_type')
    px = serializers.FloatField(source='price')
    qty = serializers.FloatField(source='quantity')
    num = serializers.IntegerField(source='number')

    class Meta:
        model = L3
        fields = ('px', 'qty', 'num', 'type_of_order')

