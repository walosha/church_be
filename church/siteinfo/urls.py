from django.urls import path
from .views import SiteInfoListAPIView

urlpatterns = [
    path('', SiteInfoListAPIView.as_view(),
         name="message_detail"),

]
