from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceListCreateAPIView, AttendanceRetrieveAPIView, AttendanceUpdateAPIView, AttendanceDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', AttendanceRetrieveAPIView.as_view(),
         name="attendance_detail"),
    path('<uuid:pk>/', AttendanceUpdateAPIView.as_view(),
         name="attendance_update"),
    path('<uuid:pk>/', AttendanceDestroyAPIView.as_view(),
         name="attendance_delete"),
    path('', AttendanceListCreateAPIView.as_view(), name="attendance_list")
]
