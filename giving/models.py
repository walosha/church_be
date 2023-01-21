from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
from .enums import STATUS
# Create your models here.


class Giving (AuditableModel):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='given')
    amount = models.IntegerField(blank=False)
    title = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=20,
                              choices=STATUS,
                              default="PENDING")
    note = models.CharField(max_length=256)
    phone = models.CharField(
        max_length=11, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField('email address')  # Here

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title
