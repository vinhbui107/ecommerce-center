from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
    UsernameField,
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomerUser
import re


class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "email", "address", "phone_number")
        field_classes = {"username": UsernameField}

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        if len(username) < 8:
            raise forms.ValidationError("Username has to be longer then 8 characters.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomerUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Your email address is not unique')
        return email


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "address", "phone_number", "photo")


class ChangePasswordForm:
    pass
