from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    address = models.CharField(default='', max_length=255)
    phone_number = models.CharField(default='', max_length=10)
