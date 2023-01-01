
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None  # Here
    email = models.EmailField('email address', unique=True)  # Here

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Here

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
