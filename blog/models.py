import time
from django.db import models
from core.models import AuditableModel
from django.utils import timezone
from account.models import CustomUser

# from .manager import PublishedManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(AuditableModel):
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

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = str(f'{self.author.firstname} {self.author.lastname}').replace(
            " ", "-").strip().lower() + '-' + str(int(time.time()))
        return super().save(*args, **kwargs)


class Comment(AuditableModel):
    postId = models.ForeignKey(Post,
                               on_delete=models.CASCADE,
                               related_name='comments')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='comments')
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'Comment by {self.author} on {self.postId}'
