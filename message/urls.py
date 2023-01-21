from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MessageListCreateAPIView, MessageRetrieveAPIView, MessageUpdateAPIView, MessageDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', MessageRetrieveAPIView.as_view(),
         name="message_detail"),
    path('<uuid:pk>/', MessageUpdateAPIView.as_view(),
         name="message_update"),
    path('<uuid:pk>/', MessageDestroyAPIView.as_view(),
         name="message_delete"),
    path('', MessageListCreateAPIView.as_view(), name="message_list")
]
