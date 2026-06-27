# =====================================================
# UNIVERSAL CRASH RECOVERY
# =====================================================

from datetime import datetime


class CrashRecovery:

    def __init__(self):

        self.crashed = False

        self.last_crash = None

        self.reason = ""

        self.total_crashes = 0


    def report_crash(

        self,

        reason

    ):

        self.crashed = True

        self.reason = reason

        self.last_crash = str(

            datetime.now()

        )

        self.total_crashes += 1


    def recover(self):

        self.crashed = False

        self.reason = ""

        return True


    def get_status(self):

        return {

            "crashed":

                self.crashed,

            "reason":

                self.reason,

            "last_crash":

                self.last_crash,

            "total_crashes":

                self.total_crashes

        }