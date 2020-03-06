from django.urls import path

from .views import *

app_name = "egx"

urlpatterns = [
    path('', home, name='home'),
    path('companies', companies, name='companies'),
]
