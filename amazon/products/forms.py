from django import forms
from products.models import *

class Product_Form(forms.Form):
    name = forms.CharField(max_length=30)
    price = forms.FloatField()