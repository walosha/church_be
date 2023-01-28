from rest_framework import serializers
from .models import VideoPodcast, AudioPodcast


class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VideoPodcast
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True},
        } 


class AudioSerializer( serializers.ModelSerializer):

    class Meta:
        model = AudioPodcast
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True},
        } 
      

