import sys

from django import forms


class ForgetPasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'email-field',
                'placeholder': 'Email'
            }
        ),
        label=''
    )


sys.modules[__name__] = ForgetPasswordForm
