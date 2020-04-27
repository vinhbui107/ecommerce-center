from django.contrib import admin
from .models import Order


@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "cart_id", "order_total", "is_complete"]
