from django.urls import path, include
from .views import EventListCreateAPIView, EventRetrieveAPIView, EventDestroyAPIView, EventUpdateAPIView,CalenderCreateAPIView

urlpatterns = [
    path('<uuid:pk>/', EventRetrieveAPIView.as_view(),
         name="event_detail"),
    path('', EventListCreateAPIView.as_view(), name="event_list"),
    path('calender/', CalenderCreateAPIView.as_view(), name="calender_create"),
    path('<uuid:pk>/', EventUpdateAPIView.as_view(), name="event_update"),
    path('<uuid:pk>/', EventDestroyAPIView.as_view(),
         name="event_delete"),
]
