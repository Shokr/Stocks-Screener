from django.urls import path

from .viewsets import *

app_name = "market"

urlpatterns = [
    path('stocks/', StockList),
    path('stocks/<int:pk>/', StockDetail),

    # path("/", view=, name=""),

]
