from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *


@login_required
def create_stock(request):
    if request.method == 'POST':
        created_stock_pk = None
        filled_form = StockForm(request.POST)
        if filled_form.is_valid():
            created_stock = filled_form.save()
            created_stock_pk = created_stock.pk
            note = 'stock %s was created' % (filled_form.cleaned_data['name'])
            filled_form = StockForm()
        else:
            note = 'stock was not created, please try again'
        new_form = StockForm()

        return render(request, 'market/add_stock.html',
                      {'StockForm': filled_form, 'note': note, 'created_stock_pk': created_stock_pk})
        # return redirect('market:list_stocks')
    else:
        form = StockForm()
        return render(request, 'market/add_stock.html', {'StockForm': form})


@login_required
def update_stock(request, pk):
    stock = Stock.objects.get(pk=pk)
    form = StockForm(instance=stock)
    if request.method == 'POST':
        filled_form = StockForm(request.POST, instance=stock)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your stock has been processed.'
            return render(request, 'market/edit_stock.html', {'StockForm': form, 'stock': stock, 'note': note})
            # return redirect('market:list_stocks')
    return render(request, 'market/edit_stock.html', {'StockForm': form, 'stock': stock})


@login_required
def view_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'market/view_stock.html', {'stock': stock})


@login_required
def list_stocks(request):
    stocks = Stock.objects.get_queryset().exclude(symbol='')
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
