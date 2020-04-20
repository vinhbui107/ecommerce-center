from django import forms
import re

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
    UsernameField
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomerUser
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'phone_number')
        field_classes = {'username': UsernameField}

    # username = forms.CharField(label="Username", max_length=30)
    # email = forms.EmailField(label="Email")
    # password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    # password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    # phone_number = forms.IntegerField(label="Your phone number")
    # address = forms.CharField(label="Address")

    # def clean_password2(self):
    #     if "password1" in self.cleaned_data:
    #         password1 = self.cleaned_data["password1"]
    #         password2 = self.cleaned_data["password2"]
    #         if password1 == password2 and password1:
    #             return password2
    #         raise forms.ValidationError("Mật khẩu không hợp lệ")
    #
    # def clean_username(self):
    #     username = self.cleaned_data["username"]
    #     if not re.search(r"^\w+$", username):
    #         raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         return username
    #     raise forms.ValidationError("Tài khoản đã tồn tại")
    #
    # def save(self):
    #     User.objects.create_user(
    #         username=self.cleaned_data["username"],
    #         email=self.cleaned_data["email"],
    #         phone_mumber=self.cleaned_data["phone_number"],
    #         address=self.cleaned_data["address"],
    #         password=self.cleaned_data["password1"],
    #     )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'address', 'phone_number')


class ChangePasswordForm():
    pass
