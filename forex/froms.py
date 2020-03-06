from django import forms

from forex.models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
