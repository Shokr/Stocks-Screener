from django.urls import path

from egx.views import home, companies

app_name = "egx"

urlpatterns = [
    path('', home, name='home'),
    path('companies', companies, name='companies'),
]
