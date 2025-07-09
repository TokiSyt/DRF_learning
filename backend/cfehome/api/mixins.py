from .permissions import IsStaffEditorPermission
from rest_framework import permissions

#Mixins are good to add anything to the views/shortcut the information provided to it 

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]