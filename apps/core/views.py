from django.views.generic import TemplateView
from django.shortcuts import render
from apps.movie.models import Movie
from django.views.generic import ListView


# class HomeView(TemplateView):
#   template_name = "core/home.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class HomeListView(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "core/home.html"
    paginate_by = 8


def error404(request, exception):
    return render(request, 'core/404.html', status=404)
