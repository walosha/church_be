# django #selenium #webscraping
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Attendance
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = '__all__'
