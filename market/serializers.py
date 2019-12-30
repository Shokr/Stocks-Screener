from rest_framework import serializers

from .models import *


# User Serializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
