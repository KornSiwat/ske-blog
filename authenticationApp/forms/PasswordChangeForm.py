import sys

from django import forms


class PasswordChangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    password1 = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'authentication-field',
                'id': 'password-field',
                'placeholder': 'New Password'
            }),
        label=''
    )

    password2 = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'authentication-field',
                'id': 'confirm-password-field',
                'placeholder': 'Confirm New Password'
            }),
        label=''
    )

    class Meta:
        fields = [
            'password1',
            'password2'
        ]


sys.modules[__name__] = PasswordChangeForm
