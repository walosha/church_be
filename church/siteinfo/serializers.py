# django #selenium #webscraping
from rest_framework import serializers
from .models import SiteInfo


class SiteInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInfo
        exclude = ["lock"]


    def to_representation(self, instance):
        print(instance)
        return super().to_representation(instance)
  
