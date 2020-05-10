from django.contrib import admin
from .models import CustomerUser


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "first_name", "last_name", "is_active"]
