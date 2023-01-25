from django.urls import path, include
from .views import VideoCreateAPIView, VideoListAPIView, VideoRetrieveAPIView, VideoDestroyAPIView, VideoUpdateAPIView, AudioListCreateAPIView, AudioRetrieveAPIView, AudioDestroyAPIView, AudioUpdateAPIView

urlpatterns = [
    path('videos/<uuid:pk>/', VideoRetrieveAPIView.as_view(),
         name="video_detail"),
    path('videos/', VideoListAPIView.as_view(), name="video_list"),
    path('videos/create', VideoCreateAPIView.as_view(), name="video_create"),
    path('videos/<uuid:pk>/', VideoUpdateAPIView.as_view(), name="video_update"),
    path('videos/<uuid:pk>/', VideoDestroyAPIView.as_view(),
         name="video_delete"),
    path('audio/<uuid:pk>/', AudioRetrieveAPIView.as_view(),
         name="audio_detail"),
    path('audio/', AudioListCreateAPIView.as_view(), name="audio_list"),
    path('audio/<uuid:pk>/', AudioUpdateAPIView.as_view(), name="audio_update"),
    path('audio/<uuid:pk>/', AudioDestroyAPIView.as_view(),
         name="audo_delete"),
]
