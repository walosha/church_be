from django.urls import path, include
from .views import EventListCreateAPIView, EventRetrieveAPIView, EventDestroyAPIView, EventUpdateAPIView

urlpatterns = [
    path('<uuid:pk>/', EventRetrieveAPIView.as_view(),
         name="event_detail"),
    path('', EventListCreateAPIView.as_view(), name="event_list"),
    path('<uuid:pk>/', EventUpdateAPIView.as_view(), name="event_update"),
    path('<uuid:pk>/', EventDestroyAPIView.as_view(),
         name="event_delete"),
]
