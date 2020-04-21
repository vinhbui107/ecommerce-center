from django.views.generic import TemplateView


class MovieDetailView(TemplateView):
    template_name = "movie/movie_detail.html"
