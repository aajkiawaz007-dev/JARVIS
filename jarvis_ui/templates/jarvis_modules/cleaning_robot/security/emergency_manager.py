# =====================================================
# UNIVERSAL EMERGENCY MANAGER
# =====================================================

from datetime import datetime


class EmergencyManager:

    def __init__(self):

        self.state = "NORMAL"

        self.reason = ""

        self.time = None


    def trigger(

        self,

        reason

    ):

        self.state = "EMERGENCY"

        self.reason = reason

        self.time = str(

            datetime.now()

        )


    def shutdown(

        self,

        reason="Emergency Shutdown"

    ):

        self.state = "SHUTDOWN"

        self.reason = reason

        self.time = str(

            datetime.now()

        )


    def warning(

        self,

        reason

    ):

        self.state = "WARNING"

        self.reason = reason

        self.time = str(

            datetime.now()

        )


    def reset(self):

        self.state = "NORMAL"

        self.reason = ""

        self.time = None


    def get_status(self):

        return {

            "state":

                self.state,

            "reason":

                self.reason,

            "time":

                self.time

        }