from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView, CreateView
from .forms import LoginForm, SignUpForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/profile/success")
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, "account/profile_update.html", {"form": form})


def profile_success(request):
    return render(request, "account/profile_success.html")


class SiteLoginView(LoginView):
    template_name = "account/login.html"


class SiteSignupView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")
