import time
from django.db import models
from core.models import AuditableModel
from django.utils import timezone
from account.models import CustomUser
from taggit.managers import TaggableManager
from .manager import PublishedManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


def generateUUID():
    return str(uuid4())


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Post(AuditableModel):
    id = models.UUIDField(
        primary_key=True, default=generateUUID, editable=False)

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    tags = TaggableManager(through=UUIDTaggedItem)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = str(f'{self.title}').replace(
            " ", "-").strip().lower() + '-' + str(int(time.time()))
        return super().save(*args, **kwargs)


class Comment(AuditableModel):
    postId = models.ForeignKey(Post,
                               on_delete=models.CASCADE,
                               related_name='comments')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='author')
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'Comment by {self.author} on {self.postId}'


class Publication(AuditableModel):
    id = models.UUIDField(
        primary_key=True, default=generateUUID, editable=False)

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='publication/%Y/%m/%d/')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='blog_publication')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    tags = TaggableManager(through=UUIDTaggedItem)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = str(f'{self.title}').replace(
            " ", "-").strip().lower() + '-' + str(int(time.time()))
        return super().save(*args, **kwargs)
