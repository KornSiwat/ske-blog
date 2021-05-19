import sys

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from authenticationApp.models import Profile


@login_required
def ProfileView(request):
    user = request.user
    profile = Profile.get_profile_by_user(user)

    if not profile.is_verified:
        return redirect(reverse('authenticationApp:account-verification'))

    context = {'profile': profile}

    return render(request, 'authenticationApp/profile.html', context)


sys.modules[__name__] = ProfileView
