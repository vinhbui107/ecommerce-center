from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Actor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="actor_photo/", blank=True)

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
    imdb_link = models.URLField(default="")
    trailer = models.URLField(default="", null=True)
    description = models.TextField()
    slug = models.SlugField(default="", unique=True)
    is_active = models.BooleanField(default=True)
    poster = models.ImageField(upload_to="movie_poster/", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie-detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("cart:remove-from-cart", kwargs={"slug": self.slug})
