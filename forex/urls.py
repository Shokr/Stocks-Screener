from django.urls import path

from forex.views import *

app_name = 'forex'

urlpatterns = [
    path('list', ListCurrencyView.as_view())
]
