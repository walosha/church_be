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
        extra_fields = ['count']

        def get_field_names(self, declared_fields, info):
            expanded_fields = super(AttendanceSerializer, self).get_field_names(
                declared_fields, info)

            if getattr(self.Meta, 'extra_fields', None):
                return expanded_fields + self.Meta.extra_fields
            else:
                return expanded_fields
