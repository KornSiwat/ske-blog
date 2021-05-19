import sys

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

from authenticationApp.models import Profile
from authenticationApp.forms import LoginForm


def LoginView(request):
    context = {'form': LoginForm}

    if request.user.is_authenticated:
        return redirect(reverse('blogApp:home'))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            profile = Profile.get_profile_by_user(user)

            if not profile.is_verified:
                return redirect(reverse('authenticationApp:account-verification'))

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            return redirect(reverse("authenticationApp:profile"))
        else:
            messages.error(request, "Incorrect username or password")

    return render(request, 'authenticationApp/login.html', context)


sys.modules[__name__] = LoginView
