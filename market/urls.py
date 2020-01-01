from django.urls import path

from .views import *
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


    path('list', list_stocks, name='list_stocks'),
    path('create', create_stock, name='create_stock'),
    path('update/<int:pk>', update_stock, name='update_stock'),
    path('delete/<int:pk>', delete_stock, name='delete_stock'),
    path('<int:pk>', view_stock, name='view_stock'),
]
