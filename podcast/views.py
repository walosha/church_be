from .models import AudioPodcast,VideoPodcast
from .serializers import VideoSerializer, AudioSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
# from django.db.models import Count

@extend_schema(
        operation_id='url',
        methods=["POST"],
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        },
                        'description': {
                        'type': 'string',
                        },
                        'url': {
                        'type': 'string',
                        'format': 'binary'
                        },
                          'time_to_watch': {
                        'type': 'number',
                        },
                        
                        
                    }
                }
            },
        )
class VideoCreateAPIView(generics.CreateAPIView):
    queryset = VideoPodcast.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser,)
    
 
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()
            
class VideoListAPIView(generics.ListAPIView):
    queryset = VideoPodcast.objects.all()
    serializer_class = VideoSerializer
    


class VideoRetrieveAPIView(generics.RetrieveAPIView):

    queryset = VideoPodcast.objects.all()
    serializer_class = VideoSerializer


class VideoUpdateAPIView(generics.UpdateAPIView):
    queryset = VideoPodcast.objects.all()
    serializer_class = VideoSerializer


class VideoDestroyAPIView(generics.DestroyAPIView):
    queryset = VideoPodcast.objects.all()
    serializer_class = VideoSerializer


# Audio
@extend_schema(
        operation_id='url-audio',
        methods=["POST"],
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        },
                        'description': {
                        'type': 'string',
                        },
                        'url': {
                        'type': 'string',
                        'format': 'binary'
                        },
                          'time_to_watch': {
                        'type': 'number',
                        },
                        
                        
                    }
                }
            },
        )
class AudioListCreateAPIView(generics.ListCreateAPIView):
    queryset = AudioPodcast.objects.all()
    serializer_class = AudioSerializer
    parser_classes = (MultiPartParser,)
    
    class Meta:
         extra_kwargs = {
            'author': {'read_only': True},
        }

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()    


class AudioRetrieveAPIView(generics.RetrieveAPIView):
    queryset = AudioPodcast.objects.all()
    serializer_class = AudioSerializer


class AudioUpdateAPIView(generics.UpdateAPIView):
    queryset = AudioPodcast.objects.all()
    serializer_class = AudioSerializer


class AudioDestroyAPIView(generics.DestroyAPIView):
    queryset = AudioPodcast.objects.all()
    serializer_class = AudioSerializer
