from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "core/home.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


def error404(request, exception):
    return render(request, 'core/404.html', status=404)
