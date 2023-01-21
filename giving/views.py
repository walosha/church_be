from .models import Giving
from .serializers import GivingSerializer
from rest_framework import generics


class GivingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Giving.objects.all()
    serializer_class = GivingSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class GivingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Giving.objects.all()
    serializer_class = GivingSerializer


class GivingUpdateAPIView(generics.UpdateAPIView):
    queryset = Giving.objects.all()
    serializer_class = GivingSerializer


class GivingDestroyAPIView(generics.DestroyAPIView):
    queryset = Giving.objects.all()
    serializer_class = GivingSerializer
