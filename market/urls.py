from django.urls import path

from .viewsets import *

app_name = "market"

urlpatterns = [
    path('stocks/', StockList, name='stocks_list'),
    path('stocks/<int:pk>/', StockDetail, name='stocks_detail'),
    path('stocks/quote/<int:pk>/', StockQuote, name='stocks_quote'),

    path('timeseries/<int:pk>/', TimeSeries, name='time_series'),
    path('timeseries/weekly/<int:pk>/', TimeSeriesWeekly, name='time_series_weely'),
    path('timeseries/monthly/<int:pk>/', TimeSeriesMonthly, name='time_series_monthly'),

    path('sectorperformances/', SectorPerformances, name='sector_performance'),

    # path("/", view=, name=""),

]
