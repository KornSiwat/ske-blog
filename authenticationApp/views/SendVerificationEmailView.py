import sys

from django.shortcuts import redirect, reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required

from authenticationApp.tokens import account_token


@login_required
def SendVerificationEmailView(request):
    user = request.user

    to_email = user.email
    mail_subject = 'Account Verification.'
    message = render_to_string('authenticationApp/mails/verificationemail.html', {
        'user': user,
        'domain': "localhost:8000",
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_token.make_token(user),
    })

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

    return redirect(reverse('authenticationApp:account-verification'))


sys.modules[__name__] = SendVerificationEmailView
