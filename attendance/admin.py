from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Attendance


class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ("id", 'eventId', "comment")
    resource_class = ImportExportModelAdmin


admin.site.register(Attendance, AttendanceAdmin)
