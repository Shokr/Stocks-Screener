from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from crypto.froms import Cryptocurrency


@login_required
def view_crypto_currency(request, pk):
    crypto_currency = get_object_or_404(Cryptocurrency, pk=pk)
    return render(request, 'crypto/viewCryptoCurrency.html', {'Cryptocurrency': crypto_currency})


@login_required
def list_crypto_currencies(request):
    crypto_currencies = Cryptocurrency.objects.get_queryset()
    return render(request, 'crypto/listCryptoCurrencies.html', {'Cryptocurrencies': crypto_currencies})
