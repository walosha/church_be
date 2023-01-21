from django.db import models
from core.models import AuditableModel
from account.models import CustomUser

# Create your models here.


class Event (AuditableModel):
    title = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='event')
    description = models.CharField(max_length=256, blank=True)
    location = models.CharField(max_length=256, blank=True)
    start_at = models.DateField()
    end_at = models.DateField()

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title
