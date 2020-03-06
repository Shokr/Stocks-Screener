from django.urls import path

from market.views import *

app_name = "market"

urlpatterns = [
    path('list', list_stocks, name='list_stocks'),
    path('create', create_stock, name='create_stock'),
    path('update/<int:pk>', update_stock, name='update_stock'),
    path('delete/<int:pk>', delete_stock, name='delete_stock'),
    path('<int:pk>', view_stock, name='view_stock'),

    path('stock_weekly/<int:pk>', view_stock_weekly, name='view_stock_weekly'),
    path('stock_monthly/<int:pk>', view_stock_monthly, name='view_stock_monthly'),

    path('sectors', sectors, name='sectors'),

]
