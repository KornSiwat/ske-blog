import sys

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(
        max_length=14,
        min_length=6,
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

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'email-field',
                'placeholder': 'Email',
                'pattern': '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
            }
        ),
        label=''
    )

    password1 = forms.CharField(
        max_length=100,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'authentication-field',
                'id': 'password-field',
                'placeholder': 'Password'
            }),
        label=''
    )

    password2 = forms.CharField(
        max_length=100,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'authentication-field',
                'id': 'confirm-password-field',
                'placeholder': 'Confirm Password'
            }),
        label=''
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


sys.modules[__name__] = RegistrationForm
