from django.urls import path
from django.conf.urls import url
# from .views import AccountViewExample
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # path('', AccountViewExample.as_view(), name='example_view'),
    path('signup/', views.signup, name="signup"),
    path('password_change_done/', views.password_change_done, name="done"),
    path('password_change_fail/', views.password_change_fail, name="fpass"),
    url(r'^password/$', views.change_password, name='change_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
