import sys

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.models import User

from authenticationApp.tokens import account_token
from authenticationApp.forms import ForgetPasswordForm


def ForgetPasswordView(request):
    context = {'form': ForgetPasswordForm}

    if request.method == "POST":
        form = ForgetPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            send_password_reset_email(email)

            messages.success(request, "Password reset link sent to " + email)
            messages.success(request, "Please check your inbox")

    return render(request, 'authenticationApp/forgetpassword.html', context)


def send_password_reset_email(email):
    user = User.objects.get(email=email)

    to_email = user.email
    mail_subject = 'Password Reset'
    message = render_to_string('authenticationApp/mails/passwordresetemail.html', {
        'user': user,
        'domain': "localhost:8000",
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_token.make_token(user),
    })

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


sys.modules[__name__] = ForgetPasswordView
