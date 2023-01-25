from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
from cloudinary.models import CloudinaryField

# Create your models here.


class SiteInfo (AuditableModel):
    meta_title = models.CharField(max_length=100, blank=False)
    meta_description = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    icon_image = CloudinaryField(resource_type='image', null=True, default=None, blank=True)
    hero_image = CloudinaryField(resource_type='image', null=True, default=None, blank=True)
    image1 = CloudinaryField(resource_type='image', null=True, default=None, blank=True)
    image2 = CloudinaryField(resource_type='image', null=True, default=None, blank=True)
    image3 = CloudinaryField(resource_type='image', null=True, default=None, blank=True)
    image4 = CloudinaryField(resource_type='video' ,null=True, default=None, blank=True)
    image5 = CloudinaryField(resource_type='video' ,null=True, default=None, blank=True)
    audio1 = CloudinaryField(resource_type='video' ,null=True, blank=True)
    audio2 = CloudinaryField(resource_type='video' ,null=True, blank=True)
    audio3 = CloudinaryField(resource_type='video' ,null=True, blank=True)
    video1 = CloudinaryField(resource_type='video', null=True, blank=True)
    video2 = CloudinaryField(resource_type='video', null=True, blank=True)
    video3 = CloudinaryField(resource_type='video', null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)
        def __str__(self) -> str:
            return self.title
