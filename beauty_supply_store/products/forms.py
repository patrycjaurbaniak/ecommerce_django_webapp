from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", 'producer', 'category', 'description', 'quantity', 'price', 'image']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', "last_name", 'password1', 'password2']