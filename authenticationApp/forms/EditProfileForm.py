import sys

from django import forms

from authenticationApp.models import Profile


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['profilepic'].required = False

    firstname = forms.CharField(
        min_length=1,
        max_length=20,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'firstname-field',
                'placeholder': 'Firstname'
            }
        ),
        label=''
    )

    lastname = forms.CharField(
        min_length=1,
        max_length=20,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'lastname-field',
                'placeholder': 'Lastname'
            }
        ),
        label=''
    )

    phone = forms.CharField(
        min_length=1,
        max_length=20,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'authentication-field',
                'id': 'phone-field',
                'placeholder': 'Phone number',
                'pattern': '^\+?[0-9]{1}[0-9]{3,14}$'
            }
        ),
        label=''
    )

    class Meta:
        model = Profile
        fields = [
            'profilepic',
            'firstname',
            'lastname',
            'phone'
        ]


sys.modules[__name__] = EditProfileForm
