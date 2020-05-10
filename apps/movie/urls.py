from django.urls import path
from .views import MovieDetailView, MovieListView, SearchMovie
from .models import Movie

app_name = "movie"

urlpatterns = [
    path("all/", MovieListView.as_view(model=Movie), name="movie-list"),
    path("<slug:the_slug>", MovieDetailView.as_view(), name="movie-detail"),
    path("search/", SearchMovie.as_view(), name="search-movie"),
]
