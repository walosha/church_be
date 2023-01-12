

from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermission ():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
