# =====================================================
# UNIVERSAL MAINTENANCE MANAGER
# =====================================================

from datetime import datetime


class MaintenanceManager:

    def __init__(self):

        self.enabled = False

        self.reason = ""

        self.started = None


    def start(

        self,

        reason="Maintenance"

    ):

        self.enabled = True

        self.reason = reason

        self.started = str(

            datetime.now()

        )


    def stop(self):

        self.enabled = False

        self.reason = ""

        self.started = None


    def is_enabled(self):

        return self.enabled


    def get_status(self):

        return {

            "enabled":

                self.enabled,

            "reason":

                self.reason,

            "started":

                self.started

        }