from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Attendance
from .resources import AttendanceAdminResource


class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ("id", 'eventId', "comment")
    resource_class = AttendanceAdminResource


admin.site.register(Attendance, AttendanceAdmin)
