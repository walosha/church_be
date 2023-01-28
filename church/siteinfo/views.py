from .models import SiteInfo
from .serializers import SiteInfoSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
# from django.db.models import Count


class SiteInfoListAPIView(generics.RetrieveAPIView):
    queryset = SiteInfo.objects.filter(lock="X")
    serializer_class = SiteInfoSerializer

    

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj