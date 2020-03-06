import requests
from django.shortcuts import render


def home(request):
    response = requests.get('https://www.mubasher.info/api/1/stocks/prices/all?country=eg')
    data = response.json()
    print(data)
    return render(request, 'egx/home.html', {'lastUpdate': data['lastUpdate'], 'prices': data['prices']})


def companies(request):
    response = requests.get('https://www.mubasher.info/api/1/listed-companies?country=eg&size=400')
    data = response.json()
    print(data['rows'])
    return render(request, 'egx/companies.html', {'companies': data['rows']})
