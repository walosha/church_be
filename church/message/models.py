from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
from .enums import QUESTION_TYPES
# Create your models here.


class Message (AuditableModel):
    title = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='message')
    body = models.TextField(blank=True)
    message_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    phone = models.CharField(
        max_length=11, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title
