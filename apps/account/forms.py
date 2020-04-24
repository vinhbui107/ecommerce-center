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


class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "email", "address", "phone_number")
        field_classes = {"username": UsernameField}


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "address", "phone_number", "photo")


class ChangePasswordForm:
    pass
