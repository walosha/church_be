# django #selenium #webscraping
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }
