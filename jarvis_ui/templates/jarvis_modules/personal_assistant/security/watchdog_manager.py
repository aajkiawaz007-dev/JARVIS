# =====================================================
# UNIVERSAL WATCHDOG MANAGER
# =====================================================

from datetime import datetime


class WatchdogManager:

    def __init__(self):

        self.last_heartbeat = None

        self.status = "ONLINE"

        self.timeout = False


    def heartbeat(self):

        self.last_heartbeat = str(

            datetime.now()

        )

        self.status = "ONLINE"

        self.timeout = False


    def report_timeout(self):

        self.status = "TIMEOUT"

        self.timeout = True


    def report_offline(self):

        self.status = "OFFLINE"


    def get_status(self):

        return {

            "status":

                self.status,

            "last_heartbeat":

                self.last_heartbeat,

            "timeout":

                self.timeout

        }