from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from .serializers import *


@permission_classes((permissions.AllowAny,))
class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
