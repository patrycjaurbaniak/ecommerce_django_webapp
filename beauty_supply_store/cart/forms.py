from django import forms

class CartAddForm(forms.Form):
    over = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)