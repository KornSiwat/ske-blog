import sys

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(
        max_length=14,
        min_length=1,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'username-field',
                'placeholder': 'Username'
            }
        ),
        label=''
    )

    password = forms.CharField(
        max_length=14,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'authentication-field',
                'id': 'password-field',
                'placeholder': 'Password'
            }
        ),
        label=''
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


sys.modules[__name__] = LoginForm
