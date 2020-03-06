from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from crypto.serializers import Cryptocurrency, CryptocurrencySerializer


@permission_classes((permissions.AllowAny,))
class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
