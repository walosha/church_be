
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, DateWidget
from .models import Attendance


class AttendanceAdminResource(resources.ModelResource):

    class Meta:
        model = Attendance
        fields = "__all__"
