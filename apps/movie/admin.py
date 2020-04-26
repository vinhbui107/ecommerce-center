from django.contrib import admin
from .models import Movie, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "price", "trailer", "is_active"]
    list_filter = ["is_active"]
    list_editable = ["price", "trailer", "is_active"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Actor)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
