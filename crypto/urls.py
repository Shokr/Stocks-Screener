from django.urls import path

from crypto.views import list_crypto_currencies, view_crypto_currency

app_name = 'crypto'

urlpatterns = [
    path('', list_crypto_currencies, name="home"),
    path('<int:pk>', view_crypto_currency, name='view_crypto_currency'),
]
