import sys

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authenticationApp.forms import PasswordChangeForm
from authenticationApp.models import Profile


@login_required
def PasswordChangeView(request):
    user = request.user
    profile = Profile.get_profile_by_user(user)

    if not profile.is_verified:
        return redirect(reverse('authenticationApp:account-verification'))

    context = {'form': PasswordChangeForm}

    if request.method == "POST":
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        is_both_password_equal = password1 == password2

        if is_both_password_equal:
            user = request.user
            new_password = password1

            user.set_password(new_password)
            user.save()

            messages.success(request, "Password changed")
            messages.success(request, "Please re-login")

            return redirect(reverse('authenticationApp:logout'))
        else:
            messages.error(request, "Password mismatch")

    return render(request, 'authenticationApp/passwordchange.html', context)


sys.modules[__name__] = PasswordChangeView
