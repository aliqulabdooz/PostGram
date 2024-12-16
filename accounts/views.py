from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout, password_validation
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import CustomUser


@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully login')
            return redirect(user.get_absolute_url())
        else:
            messages.error(request, 'username or password is incorrect')
            context = {
                'url_name': request.resolver_match.url_name,
            }
            return render(request, 'accounts/login-register.html', context)
    else:
        return render(request, "accounts/login-register.html")


def logout_view(request):
    logout(request)
    return redirect('network:index_view')


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            error_message = 'Passwords must match.'
        else:
            try:
                password_validation.validate_password(password)
            except ValidationError as e:
                messages.error(request, e.messages.pop())
            else:
                # Attempt to create new user
                try:
                    user = CustomUser.objects.create_user(username=username, password=password, email=email)
                    user.save()
                except IntegrityError:
                    messages.error(request, "username already taken")
                else:
                    login(request, user)
                    return redirect(user.get_absolute_url())

        context = {
            'url_name': request.resolver_match.url_name,

        }
        return render(request, 'accounts/login-register.html', context)
    else:
        return render(request, "accounts/login-register.html")
