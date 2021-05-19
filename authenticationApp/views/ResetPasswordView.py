import sys

from django.shortcuts import redirect, reverse
from django.contrib.auth import login
from django.contrib import messages

from authenticationApp.views import get_user_by_uid_token
from authenticationApp.tokens import account_token


def ResetPasswordView(request, uidb64, token):
    user = get_user_by_uid_token(uidb64, token)

    if user is not None and account_token.check_token(user, token):
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect(reverse('authenticationApp:password-change'))
    else:
        messages.error(request, "Invalid Link")

    return redirect(reverse('authenticationApp:login'))


sys.modules[__name__] = ResetPasswordView
