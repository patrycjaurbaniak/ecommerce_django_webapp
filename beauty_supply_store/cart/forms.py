from django import forms


product_quantity=[(i,str(i)) for i in range(1, 11)]
class CartAddForm(forms.Form):
    over = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    quantity = forms. TypedChoiceField(choices=product_quantity, coerce=int)