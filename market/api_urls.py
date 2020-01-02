from django.urls import path

from .viewsets import *

app_name = "market"

urlpatterns = [
    path('stocks/', StockList, name='StockList'),
    path('stocks/<int:pk>/', StockDetail, name='StockDetail'),

    path('stocks/quote/<int:pk>/', StockQuote, name='StockQuote'),

    path('timeseries/<int:pk>/', TimeSeries, name='TimeSeries'),
    path('timeseries/weekly/<int:pk>/', TimeSeriesWeekly, name='TimeSeriesWeekly'),
    path('timeseries/monthly/<int:pk>/', TimeSeriesMonthly, name='TimeSeriesMonthly'),

    path('sectorperformances/', SectorPerformances, name='SectorPerformances'),
]