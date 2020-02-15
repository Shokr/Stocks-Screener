from django import forms

from .models import *


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
