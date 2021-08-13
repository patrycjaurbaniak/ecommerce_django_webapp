from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", 'producer', 'category', 'description', 'quantity', 'price', 'image']