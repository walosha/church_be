from django.utils.translation import gettext_lazy as _
from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
import  datetime
from cloudinary.models import CloudinaryField


# Create your models here.

class Base (AuditableModel):
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='%(class)s_related',)
    description = models.CharField(max_length=256, blank=True)
    url = CloudinaryField(resource_type='video',null=False, blank=False)
    time_to_watch =models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title


class VideoPodcast (Base):
  pass



class AudioPodcast (Base):
    pass
