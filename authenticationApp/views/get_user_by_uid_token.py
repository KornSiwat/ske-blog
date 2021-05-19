import sys

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth.models import User


def get_user_by_uid_token(uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    return user


sys.modules[__name__] = get_user_by_uid_token
