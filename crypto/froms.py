from django import forms

from crypto.models import Cryptocurrency


class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'
