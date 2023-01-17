from django.contrib import admin
from .models import Event
from import_export.admin import ImportExportModelAdmin


class EventAdmin(ImportExportModelAdmin):
    list_display = ('title', "description", "start_at",
                    "start_at", "created_at")
    resource_class = ImportExportModelAdmin


admin.site.register(Event, EventAdmin)
