import sys

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages

from authenticationApp.models import Profile
from authenticationApp.forms import RegistrationForm


def RegistrationView(request):
    context = {'form': RegistrationForm}

    if request.user.is_authenticated:
        return redirect(reverse('blogApp:home'))

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            profile = Profile.get_profile_by_user(user)
            profile.is_verified = False
            profile.save()

            return redirect(reverse('authenticationApp:account-verification'))
        else:
            is_username_already_exist = User.objects.filter(
                username=form['username'].value()).count() != 0
            is_email_already_exist = User.objects.filter(
                email=form['email'].value()).count() != 0
            is_password_mismatch = form['password1'].value(
            ) != form['password2'].value()

            if is_username_already_exist:
                messages.error(request, "Username is taken")
            if is_email_already_exist:
                messages.error(request, "Email is taken")
            if is_password_mismatch:
                messages.error(request, "Password mismatch")

    return render(request, 'authenticationApp/registration.html', context)


sys.modules[__name__] = RegistrationView
