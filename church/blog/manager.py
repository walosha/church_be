from django.db import models
# from .models import Post


class PublishedManager(models.Manager):
    def get_queryset(self, instance):
        return super().get_queryset().filter(status=instance.Status.PUBLISHED)
