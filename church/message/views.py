from .models import Message
from .serializers import MessageSerializer
from rest_framework import generics


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class MessageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateAPIView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDestroyAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
