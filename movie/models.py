from django.db import models
from django.utils.text import slugify


class Actor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    director = models.CharField(max_length=30)
    actors = models.ManyToManyField(Actor)
    genres = models.CharField(max_length=100)
    country = models.CharField(max_length=5)
    year = models.CharField(max_length=4)
    imdb_score = models.DecimalField(max_digits=9, decimal_places=2)
    imdb_link = models.URLField(default='')
    poster = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(default='Default', unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
