from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
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


def register_user(request):
    """ User registration view
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":

            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + username)
                return redirect('login')
        return render(request, "register.html", {'form': form})


def login_user(request):
    """ User login view
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_user(request):
    """ User logout
    """
    logout(request)
    return redirect('login')


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


def contact(request):
    """ View presenting contact form
    """
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        send_mail(message_name, message, message_email, [''])
        return render(request, 'contact_thanks.html', {})
    else:
        return render(request, 'contact.html')


@login_required(redirect_field_name='login')
def change_password(request):
    message=""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            message="Your password has been changed!"
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form, 'message': message})

