from rest_framework import generics

from forex.serializers import Currency, CurrencySerializer


# Create your views here.


class ListCurrencyView(generics.ListAPIView):
    queryset = Currency.objects.all()  # used for returning objects from this view
    serializer_class = CurrencySerializer
