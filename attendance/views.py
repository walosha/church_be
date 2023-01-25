from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework import generics
from core.permissions import IsAdmin


class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAdmin,)


class AttendanceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAdmin,)


class AttendanceUpdateAPIView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAdmin,)


class AttendanceDestroyAPIView(generics.DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAdmin,)
