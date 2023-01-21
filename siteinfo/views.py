from .models import SiteInfo
from .serializers import SiteInfoSerializer
from rest_framework import generics
# from django.db.models import Count


class SiteInfoListAPIView(generics.ListAPIView):
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
