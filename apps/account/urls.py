from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    profile,
    profile_success,
    ConfirmSignupView,
    ConfirmEmailNotification,
    ConfirmEmailSuccess,
)

app_name = "account"

urlpatterns = [
    path("profile/", profile, name="update_profile"),
    path("profile/success/", profile_success, name="profile_success"),
    # registration
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
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
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path('confirm-email/<str:user_id>/<str:token>/', ConfirmSignupView.as_view(), name='confirm_email'),
    path('confirm-email/success/', ConfirmEmailSuccess.as_view(), name="confirm_email_success"),
    path('confirm-email/noti/', ConfirmEmailNotification.as_view(), name="confirm_email_noti"),
]
