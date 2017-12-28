from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class EmailRegistrationForm(UserCreationForm):
    """Class for email registration form."""
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Please provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')