from django.urls import path

from .views import *

app_name = 'forex'

urlpatterns = [
    path('list', ListCurrencyView.as_view())
]
