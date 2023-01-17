from django.db import models
from event.models import Event
from core.models import AuditableModel


class Attendance (AuditableModel):
    eventId = models.ForeignKey(
        Event, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.id
