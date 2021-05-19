import sys

from django.shortcuts import redirect, reverse
from django.contrib.auth import login
from django.contrib import messages

from authenticationApp.views import get_user_by_uid_token
from authenticationApp.tokens import account_token
from authenticationApp.models import Profile


def VerifyAccountView(request, uidb64, token):
    user = get_user_by_uid_token(uidb64, token)

    if user is not None and account_token.check_token(user, token):
        Profile.verify_profile_by_user(user)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        messages.success(request, "Verification Success")
    else:
        messages.error(request, "Invalid Link")

    return redirect(reverse('authenticationApp:account-verification'))


sys.modules[__name__] = VerifyAccountView
