from django.urls import path

from .views import *

app_name = "market"

urlpatterns = [
    path('list', list_stocks, name='list_stocks'),
    path('create', create_stock, name='create_stock'),
    path('update/<int:pk>', update_stock, name='update_stock'),
    path('delete/<int:pk>', delete_stock, name='delete_stock'),
    path('<int:pk>', view_stock, name='view_stock'),

    path('chart/', testing, name='test'),

]
