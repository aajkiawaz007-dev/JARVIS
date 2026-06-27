# =====================================================
# UNIVERSAL SECURITY MANAGER
# =====================================================

class SecurityManager:

    def __init__(self):

        self.security_enabled = True

        self.safe_mode = True

        self.debug_mode = False

        self.module_locked = False


    def get_status(self):

        return {

            "security_enabled":
                self.security_enabled,

            "safe_mode":
                self.safe_mode,

            "debug_mode":
                self.debug_mode,

            "module_locked":
                self.module_locked
        }


    def lock_module(self):

        self.module_locked = True


    def unlock_module(self):

        self.module_locked = False


    def enable_debug(self):

        self.debug_mode = True


    def disable_debug(self):

        self.debug_mode = False