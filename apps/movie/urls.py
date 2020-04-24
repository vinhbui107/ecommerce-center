from django.urls import path
from .views import MovieDetailView, MovieListView


app_name = "movie"

urlpatterns = [
    path("all/", MovieListView.as_view(), name="movie-list"),
    path("<slug:the_slug>", MovieDetailView.as_view(), name="movie-detail"),
]
