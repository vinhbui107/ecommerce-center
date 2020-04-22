from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView
from .forms import LoginForm, SignUpForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.views import generic


def profile(request):
    user = request.user
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/successprofile")
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, "account/profile.html", {"form": form})


def successprofile(request):
    return render(request, "account/successprofile.html")


class SiteLoginView(LoginView):
    template_name = "account/login.html"


class SiteSignupView(generic.CreateView):
    template_name = "account/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignUpForm


class UpdateProfileView:
    pass


class UpdateProfileDoneView:
    pass


class ChangePasswordFailView:
    pass
