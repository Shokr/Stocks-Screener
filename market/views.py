from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

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
    return render(request, 'market/view_stock.html', {'stock': stock})


@login_required
def list_stocks(request):
    stocks = Stock.objects.get_queryset().exclude(symbol=None)
    return render(request, 'market/list_stocks.html', {'stocks': stocks})


@login_required
def delete_stock(request, pk):
    stock = Stock.objects.get(pk=pk)
    stock.delete()
    return redirect('market:list_stocks')


####################################################################################################################
####################################################################################################################
@login_required
def view_stock_weekly(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'market/view_stock_weekly.html', {'stock': stock})


@login_required
def view_stock_monthly(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'market/view_stock_monthly.html', {'stock': stock})


@login_required
def sectors(request):
    return render(request, 'market/sector_performances.html')
