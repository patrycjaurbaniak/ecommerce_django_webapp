from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from products.models import *
from .cart import Cart
from .forms import CartAddForm
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add_cart(products=product, quantity=cleaned_data['quantity'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove_cart(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    categories = Categories.objects.all()
    cart = Cart(request)
    categories_data = {'categories': categories, 'cart': cart}
    return render(request, 'cart.html', categories_data)
