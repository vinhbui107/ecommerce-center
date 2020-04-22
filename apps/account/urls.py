from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    profile,
    successprofile,
)

app_name = "account"

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("successprofile/", successprofile, name="successprofile"),
    # registration
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'),
        name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
