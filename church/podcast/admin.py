from django.contrib import admin
from .models import VideoPodcast,AudioPodcast
from import_export.admin import ImportExportModelAdmin


class VideoAdmin(ImportExportModelAdmin):
    list_display = ('title', "description", "time_to_watch","url",
                    "author")
    resource_class = ImportExportModelAdmin


admin.site.register(VideoPodcast, VideoAdmin)


class VideoAdmin(ImportExportModelAdmin):
    list_display = ('title', "description", "time_to_watch","url",
                    "author")
    resource_class = ImportExportModelAdmin


admin.site.register(AudioPodcast,VideoAdmin)