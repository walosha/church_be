from django.contrib import admin
from .models import Poll, PollCategory, PollQuestion, PollResponse, PollQuestionOption

admin.site.register(Poll)
admin.site.register(PollCategory)
admin.site.register(PollQuestion)
admin.site.register(PollResponse)
admin.site.register(PollQuestionOption)
