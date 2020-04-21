from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
