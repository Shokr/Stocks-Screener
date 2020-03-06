from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from forex.serializers import Currency, CurrencySerializer


@permission_classes((permissions.AllowAny,))
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
