# django #selenium #webscraping
from rest_framework import serializers
from .models import SiteInfo


class SiteInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInfo
        fields = '__all__'
