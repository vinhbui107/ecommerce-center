from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

mobile_regex = RegexValidator(
    regex=r'^(\+\d{1,3})?,?\s?\d{10,13}',
    message="Phone number must not consist of space and requires country code. eg : +84345678900")


class CustomerUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(validators=[mobile_regex], max_length=13, blank=True)
    photo = models.ImageField(upload_to="profile/", blank=True)
