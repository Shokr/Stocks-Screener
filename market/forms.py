from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
