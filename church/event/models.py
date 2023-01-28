from django.utils.translation import gettext_lazy as _
from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
import  datetime

# Create your models here.


class Event (AuditableModel):
    title = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='event')
    description = models.CharField(max_length=256, blank=True)
    location = models.CharField(max_length=256, blank=True)
    start_date_at = models.DateField(("Date"), default=datetime.date.today)
    start_time_at = models.TimeField(default=datetime.time(00, 00))
    end_date_at = models.DateField(("Date"), default=datetime.date.today)
    end_time_at = models.TimeField(default=datetime.time(00, 00))

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title
