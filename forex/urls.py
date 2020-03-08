from django.urls import path

from forex.views import *

app_name = 'forex'

urlpatterns = [
    path('', list_currencies, name="home"),
    path('<int:pk>', view_currency, name='view_currency'),

    # path('list', ListCurrencyView.as_view())
]
