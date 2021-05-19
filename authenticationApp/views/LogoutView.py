import sys

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.contrib.auth import logout as django_logout

@login_required
def LogoutView(request):
    django_logout(request)

    return redirect('authenticationApp:login')


sys.modules[__name__] = LogoutView