from django.urls import path

from .viewsets import *

app_name = "market"

urlpatterns = [
    path('stocks/', StockList),
    path('stocks/<int:pk>/', StockDetail),

    path('timeseries/<int:pk>/', TimeSeries),
    path('timeseries/weekly/<int:pk>/', TimeSeriesWeekly),
    path('timeseries/monthly/<int:pk>/', TimeSeriesMonthly),

    path('sectorperformances/', SectorPerformances),

    # path("/", view=, name=""),

]
