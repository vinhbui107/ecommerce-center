from django.contrib import admin
from .models import Cart, CartMovie


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "create_date", "update_date", "is_active"]


@admin.register(CartMovie)
class CartMovieAdmin(admin.ModelAdmin):
    list_display = ["user_id", "movie", "is_active"]
