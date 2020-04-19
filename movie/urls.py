from django.urls import path
from .views import MovieDetailView


app_name = "movie"

urlpatterns = [
    path("test/", MovieDetailView.as_view(), name="detail-movie"),
]
