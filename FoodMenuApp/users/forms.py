from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    description = forms.CharField(max_length= 250)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'description']

        help_text = {
            'username': None,
            'password1': None
        }