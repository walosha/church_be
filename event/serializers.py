# django #selenium #webscraping
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = '__all__'
        extra_kwargs = {
             'owner': {'read_only': True},
        }     
       
