from rest_framework import serializers

from .models import *


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['cryptocurrency', 'price', 'market_cap', 'change']
