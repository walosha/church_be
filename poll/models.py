from django.db import models
from core.models import AuditableModel
from account.models import CustomUser
from .enums import POLL_STATUS, QUESTION_TYPES
# Create your models here.


class PollCategory(AuditableModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.name


class Poll(AuditableModel):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(PollCategory, on_delete=models.SET_DEFAULT, max_length=20,
                             null=False, blank=False, default='GENRIC')
    start_date = models.DateField()
    end_date = models.DateField()
    poll_instruction = models.TextField(null=True)
    status = models.CharField(
        max_length=255, choices=POLL_STATUS, default='DRAFT')

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.name


class PollQuestion(AuditableModel):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    position = models.IntegerField(default=0)
    required = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    class Meta:
        ordering = ('created_at',)


class PollQuestionOption(AuditableModel):
    question = models.ForeignKey(
        PollQuestion, on_delete=models.CASCADE, related_name='question_option')
    value = models.CharField(max_length=100)
    key = models.CharField(max_length=100, null=True)
    max_field_rating = models.IntegerField(default=0)

    class Meta:
        ordering = ('created_at',)


class PollResponse(AuditableModel):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='poll_response',
        null=True)
    question = models.ForeignKey(
        PollQuestion, on_delete=models.CASCADE, null=True)
    selected_options = models.ManyToManyField(
        PollQuestionOption)  # This will have to be an array
    comment = models.CharField(null=True, blank=True, max_length=1000)

    class Meta:
        ordering = ('created_at',)
