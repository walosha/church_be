from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GivingListCreateAPIView, GivingRetrieveAPIView, GivingUpdateAPIView, GivingDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', GivingRetrieveAPIView.as_view(),
         name="giving_detail"),
    path('<uuid:pk>/', GivingUpdateAPIView.as_view(),
         name="giving_update"),
    path('<uuid:pk>/', GivingDestroyAPIView.as_view(),
         name="giving_delete"),
    path('', GivingListCreateAPIView.as_view(), name="giving_list")
]
