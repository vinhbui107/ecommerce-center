from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView
from .forms import (
    LoginForm,
    SignUpForm,
    UpdateProfileForm
)


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdataProfileForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/successprofile')
    else:
        form = UpdataProfileForm(instance=user)

    return render(request, "account/profile.html", {'form': form})


def successprofile(request):
    return render(request, "account/successprofile.html")


class SiteLoginView(LoginView):
    template_name = "account/login.html"


class SiteSignupView(FormView):
    template_name = 'account/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        from pprint import pprint; pprint(data)


class UpdateProfileView():
    pass


class UpdateProfileDoneView():
    pass


class ChangePasswordView():
    pass


class ChangePasswordDoneView():
    pass


class ChangePasswordFailView():
    pass


# def change_password(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, ("mat khau da duoc cap nhat!"))
#             return HttpResponseRedirect("/account/password_change_done")
#         else:
#             messages.error(request, ("Please correct the error below."))
#             return HttpResponseRedirect("/account/password_change_fail")
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, "account/change_password.html", {"form": form})
#
#
# def password_change_done(request):
#     return render(request, "account/password_change_done.html")
#
#
# def password_change_fail(request):
#     return render(request, "account/password_change_fail.html")
