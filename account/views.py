from django.shortcuts import render

from django.views.generic import TemplateView


class AccountViewExample(TemplateView):
    template_name = 'account/signup.html'
