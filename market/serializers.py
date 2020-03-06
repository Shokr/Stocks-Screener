from rest_framework import serializers

from market.models import Stock


# User Serializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
