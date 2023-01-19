
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from .enums import CATEGORY, ROLES


class CustomUser(AbstractUser):
    username = None  # Here
    email = models.EmailField('email address', unique=True)  # Here
    firstname = models.CharField(max_length=256)  # Here
    lastname = models.CharField(max_length=256)  # Here
    role = models.CharField(max_length=50, choices=ROLES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    category = models.CharField(
        default='unknown', max_length=20, choices=CATEGORY)
    objects = CustomUserManager()  # Here

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
