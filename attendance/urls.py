from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceListCreateAPIView, AttendanceRetrieveAPIView

urlpatterns = [
    path('<int:pk>/', AttendanceRetrieveAPIView.as_view(),
         name="attendance_detail"),
    path('', AttendanceListCreateAPIView.as_view(), name="attendance_list")
]
