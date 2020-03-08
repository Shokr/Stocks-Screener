from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from forex.froms import Currency


@login_required
def view_currency(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    return render(request, 'forex/viewCurrency.html', {'Currency': currency})


@login_required
def list_currencies(request):
    currencies = Currency.objects.get_queryset()
    return render(request, 'forex/listCurrencies.html', {'Currencies': currencies})


# from rest_framework import generics
#
# from forex.serializers import Currency, CurrencySerializer
#
#
# # # # # # # # #
# class ListCurrencyView(generics.ListAPIView):
#     queryset = Currency.objects.all()  # used for returning objects from this view
#     serializer_class = CurrencySerializer
#
