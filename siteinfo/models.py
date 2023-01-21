from django.db import models
from core.models import AuditableModel
from account.models import CustomUser

# Create your models here.


class SiteInfo (AuditableModel):
    meta_title = models.CharField(max_length=100, blank=False)
    meta_description = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    icon_image = models.ImageField(upload_to='site/%Y/%m/%d/')
    hero_image = models.ImageField(upload_to='site/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='site/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='site/%Y/%m/%d/',null=True, blank=True)
    image3 = models.ImageField(upload_to='site/%Y/%m/%d/',null=True, blank=True)
    image4 = models.ImageField(upload_to='site/%Y/%m/%d/',null=True, blank=True)
    image5 = models.ImageField(upload_to='site/%Y/%m/%d/',null=True, blank=True)
    audio1 = models.FileField(upload_to='audio/', null=True, blank=True)
    audio2 = models.FileField(upload_to='audio/', null=True, blank=True)
    audio3 = models.FileField(upload_to='audio/', null=True, blank=True)
    video1 = models.FileField(upload_to='videos/', null=True, blank=True)
    video2 = models.FileField(upload_to='videos/', null=True, blank=True)
    video3 = models.FileField(upload_to='videos/', null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

        def __str__(self) -> str:
            return self.title
