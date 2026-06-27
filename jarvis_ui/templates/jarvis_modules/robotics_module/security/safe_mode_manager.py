# =====================================================
# UNIVERSAL SAFE MODE MANAGER
# =====================================================

from datetime import datetime


class SafeModeManager:

    def __init__(self):

        self.safe_mode = False

        self.reason = ""

        self.started = None


    def enable(

        self,

        reason

    ):

        self.safe_mode = True

        self.reason = reason

        self.started = str(

            datetime.now()

        )


    def disable(self):

        self.safe_mode = False

        self.reason = ""

        self.started = None


    def is_enabled(self):

        return self.safe_mode


    def get_status(self):

        return {

            "safe_mode":

                self.safe_mode,

            "reason":

                self.reason,

            "started":

                self.started

        }