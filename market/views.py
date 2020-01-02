from bokeh.embed import components
from bokeh.layouts import column
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from StocksScreener.settings import AlphaVantagekey as key
from .forms import *


@login_required
def create_stock(request):
    if request.method == 'POST':
        filled_form = StockForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_stock = filled_form.save()
            filled_form = StockForm()
        else:
            new_form = StockForm()

        return redirect('market:list_stocks')
    else:
        form = StockForm()
        return render(request, 'market/add_stock.html', {'StockForm': form})


@login_required
def update_stock(request, pk):
    stock = Stock.objects.get(pk=pk)
    form = StockForm(instance=stock)
    if request.method == 'POST':
        filled_form = StockForm(request.POST, request.FILES, instance=stock)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            return redirect('market:list_stocks')
    return render(request, 'market/edit_stock.html', {'StockForm': form, 'stock': stock})


@login_required
def view_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    # from alpha_vantage.timeseries import TimeSeries
    # ts = TimeSeries(key=key)
    # data, meta_data = ts.get_daily(symbol=stock.symbol, outputsize='compact')
    # https://medium.com/harinathselvaraj/visualizing-stock-market-data-in-python-5e049feb1a54
    return render(request, 'market/view_stock.html', {'stock': stock})


@login_required
def list_stocks(request):
    stocks = Stock.objects.get_queryset()
    return render(request, 'market/list_stocks.html', {'stocks': stocks})


@login_required
def delete_stock(request, pk):
    stock = Stock.objects.get(pk=pk)
    stock.delete()
    return redirect('market:list_stocks')


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# Importing Libraries
import requests
import pandas as pd
from bokeh.plotting import figure
from math import pi


# # Code to obtain trade data for AAPL
# stock_name = 'AAPL'
# r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_name + '&apikey=' + key)
# print(r.status_code)
# result = r.json()
# dataForAllDays = result['Time Series (Daily)']
#
# # convert to dataframe
# df = pd.DataFrame.from_dict(dataForAllDays, orient='index')
# df = df.reset_index()
# # rename columns
# df = df.rename(index=str,
#                columns={"index": "date", "1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close",
#                         "5. volume": "volume"})
# # Changing to datetime
# df['date'] = pd.to_datetime(df['date'])
# # Sort according to date
# df = df.sort_values(by=['date'])
# # Changing the datatype
# df.open = df.open.astype(float)
# df.close = df.close.astype(float)
# df.high = df.high.astype(float)
# df.low = df.low.astype(float)
# df.volume = df.volume.astype(int)
# # check the data
# df.head()
# # Check the datatype
# df.info()
#
# inc = df.close > df.open
# dec = df.open > df.close
# w = 12 * 60 * 60 * 1000  # half day in ms
# TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
# title = stock_name + ' Chart'
# p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title=title)
# p.xaxis.major_label_orientation = pi / 4
# p.grid.grid_line_alpha = 0.3
# p.segment(df.date, df.high, df.date, df.low, color="black")
# p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
# p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")
# # Store as a HTML file
# output_file("stock_information.html", title="candlestick.py example")
# # Display in browser
# show(p)

def testing(request):
    # Code to obtain trade data for AAPL
    stock_name = 'AAPL'
    r = requests.get(
        'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_name + '&apikey=' + key)
    print(r.status_code)
    result = r.json()
    dataForAllDays = result['Time Series (Daily)']

    # convert to dataframe
    df = pd.DataFrame.from_dict(dataForAllDays, orient='index')
    df = df.reset_index()
    # rename columns
    df = df.rename(index=str,
                   columns={"index": "date", "1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close",
                            "5. volume": "volume"})
    # Changing to datetime
    df['date'] = pd.to_datetime(df['date'])
    # Sort according to date
    df = df.sort_values(by=['date'])
    # Changing the datatype
    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    df.volume = df.volume.astype(int)
    # check the data
    df.head()
    # Check the datatype
    df.info()

    inc = df.close > df.open
    dec = df.open > df.close
    w = 12 * 60 * 60 * 1000  # half day in ms
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    title = stock_name + ' Chart'
    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title=title)
    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3
    p.segment(df.date, df.high, df.date, df.low, color="black")
    p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(column(p, ))

    return render(request, 'charts.html', {'script': script, 'div': div})
