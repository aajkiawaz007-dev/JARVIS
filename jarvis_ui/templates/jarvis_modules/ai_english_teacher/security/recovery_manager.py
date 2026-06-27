# =====================================================
# UNIVERSAL RECOVERY MANAGER
# =====================================================

from security.health_monitor import HealthMonitor
from security.crash_recovery import CrashRecovery
from security.safe_mode_manager import SafeModeManager
from security.emergency_manager import EmergencyManager


class RecoveryManager:

    def __init__(self):

        self.health = HealthMonitor()

        self.crash = CrashRecovery()

        self.safe_mode = SafeModeManager()

        self.emergency = EmergencyManager()


    def recover(self):

        self.crash.recover()

        self.safe_mode.disable()

        self.emergency.reset()

        self.health.clear()

        return True


    def get_system_status(self):

        return {

            "health":
                self.health.check(),

            "crash":
                self.crash.get_status(),

            "safe_mode":
                self.safe_mode.get_status(),

            "emergency":
                self.emergency.get_status()

        }