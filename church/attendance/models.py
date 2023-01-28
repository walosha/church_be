from django.db import models
from event.models import Event
from account.models import CustomUser
from core.models import AuditableModel


class Attendance (AuditableModel):
    eventId = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, related_name='event_attendance')
    attendees = models.ManyToManyField(CustomUser)
    comment = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.id)

    def count(self):
        return self.attendees.count()
