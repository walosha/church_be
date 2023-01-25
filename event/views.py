from rest_framework import generics
from .serializers import EventSerializer
from .models import Event


class EventListCreateAPIView (generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class EventRetrieveAPIView (generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDestroyAPIView (generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventUpdateAPIView (generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
