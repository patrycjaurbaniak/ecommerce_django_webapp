from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddForm



def index(request):
    """ Main view of the application which includes other subviews
    """
    categories = Categories.objects.all()
    categories_data = {'categories': categories}
    return render(request, "index.html", categories_data)


def home(request):
    """ View presenting the homepage
    """
    categories = Categories.objects.all()
    categories_data = {'categories': categories}
    return render(request, 'home.html', categories_data)


def category(request, id):
    """ View presenting details of the selected by user category
    """
    category_user = Categories.objects.get(pk=id)
    categories = Categories.objects.all()
    category_product = Products.objects.filter(category=category_user)
    categories_data = {'categories': categories,
                       'category_product': category_product,
                       'category_user': category_user}
    return render(request, 'category_product.html', categories_data)


def product_id(request, id):
    """ View presenting details of the selected by user product
    """
    product_user = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()
    cart_product_form = CartAddForm()

    products_data = {'product_user': product_user, 'categories': categories, 'cart_product_form': cart_product_form}
    return render(request, "product.html", products_data)


def search(request):
    """ View presenting searched products
    """
    categories = Categories.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searched_product = Products.objects.all().filter(title__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'searched_product': searched_product,
                                               'categories': categories})
    else:
        return render(request, 'search.html', {'categories': categories})



