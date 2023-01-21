
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from .enums import CATEGORY, ROLES
from core.models import AuditableModel
from django.contrib.auth.models import PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
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
        ordering = ('-id',)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class ChurchGroup(AuditableModel):
    name = models.CharField(max_length=256)
    purpose = models.CharField(max_length=256)  # Here
    leader = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='leader')
    members = models.ManyToManyField(
        CustomUser, related_name="group_list", blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.name}'
