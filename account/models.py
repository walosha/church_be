
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from .enums import category


class CustomUser(AbstractUser):
    username = None  # Here
    email = models.EmailField('email address', unique=True)  # Here
    firstname = models.CharField(max_length=256)  # Here
    lastname = models.CharField(max_length=256)  # Here
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    category = models.CharField(
        default='unknown', max_length=20, choices=category)
    objects = CustomUserManager()  # Here

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
