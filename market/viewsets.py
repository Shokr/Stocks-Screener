# from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from StocksScreener.settings import AlphaVantagekey as key
from .serializers import *


@permission_classes((permissions.IsAuthenticated,))
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


####################################################################################################################3
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def StockList(request, format=None):
    """
    List all code Stock, or create a new Wallet.
    """
    if request.method == 'GET':
        Stocks = Stock.objects.all()
        serializer = StockSerializer(Stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def StockDetail(request, pk, format=None):
    """
    Retrieve, update or delete a code Stock.
    """
    try:
        StockData = Stock.objects.get(pk=pk)
    except StockData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(StockData)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StockSerializer(StockData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Stock.delete(StockData)
        return Response(status=status.HTTP_204_NO_CONTENT)


####################################################################################################################3
@csrf_exempt
@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def StockQuote(request, pk, format=None):
    try:
        symbol = Stock.objects.get(pk=pk).symbol
    except symbol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        from alpha_vantage.timeseries import TimeSeries
        ts = TimeSeries(key=key)
        try:
            data, meta_data = ts.get_quote_endpoint(symbol=symbol)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data)


@csrf_exempt
@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def TimeSeries(request, pk, format=None):
    try:
        symbol = Stock.objects.get(pk=pk).symbol
    except symbol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        from alpha_vantage.timeseries import TimeSeries
        ts = TimeSeries(key=key)
        try:
            data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
            # return Response({'ERROR': 'Stock not found'})
        return Response(data)


@csrf_exempt
@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def TimeSeriesWeekly(request, pk, format=None):
    try:
        symbol = Stock.objects.get(pk=pk).symbol
    except symbol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        from alpha_vantage.timeseries import TimeSeries
        ts = TimeSeries(key=key)
        try:
            data, meta_data = ts.get_weekly_adjusted(symbol=symbol)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data)


@csrf_exempt
@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def TimeSeriesMonthly(request, pk, format=None):
    try:
        symbol = Stock.objects.get(pk=pk).symbol
    except symbol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        from alpha_vantage.timeseries import TimeSeries
        ts = TimeSeries(key=key)
        try:
            data, meta_data = ts.get_monthly(symbol=symbol)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data)


@csrf_exempt
@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def SectorPerformances(request, format=None):
    if request.method == 'GET':
        from alpha_vantage.sectorperformance import SectorPerformances
        sp = SectorPerformances(key=key)
        data, meta_data = sp.get_sector()
        return Response(data)

# urlpatterns = format_suffix_patterns(urlpatterns)
