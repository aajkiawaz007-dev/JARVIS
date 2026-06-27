# =====================================================
# UNIVERSAL ACCESS CONTROL MANAGER
# =====================================================

from security.permission_manager import PermissionManager


class AccessControlManager:

    def __init__(self):

        self.permissions = PermissionManager()


    def allow(self, permission):

        return self.permissions.has_permission(
            permission
        )


    def deny(self, permission):

        return not self.allow(
            permission
        )


    def require(self, permission):

        if self.allow(permission):

            return True

        raise PermissionError(

            f"Permission denied : {permission}"

        )