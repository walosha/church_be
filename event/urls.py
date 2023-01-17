from django.urls import path, include
from .views import EventListCreateAPIView, EventRetrieveAPIView

urlpatterns = [
    path('<int:pk>/', EventRetrieveAPIView.as_view(),
         name="event_detail"),
    path('', EventListCreateAPIView.as_view(), name="event_list")
]
