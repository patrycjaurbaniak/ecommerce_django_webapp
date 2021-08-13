from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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


@login_required(redirect_field_name='login')
def change_password(request):
    """ View allowing the user to change the password
    """
    message=""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            message = "Your password has been changed!"
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form, 'message': message})


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