# =====================================================
# UNIVERSAL HEALTH MONITOR
# =====================================================

from datetime import datetime


class HealthMonitor:

    def __init__(self):

        self.status = "Healthy"

        self.last_check = None

        self.message = "System OK"

        self.errors = []

        self.warnings = []


    def check(self):

        self.last_check = str(

            datetime.now()

        )

        return {

            "status":

                self.status,

            "last_check":

                self.last_check,

            "message":

                self.message,

            "warnings":

                self.warnings,

            "errors":

                self.errors

        }


    def set_status(

        self,

        status,

        message=""

    ):

        self.status = status

        self.message = message


    def add_warning(

        self,

        warning

    ):

        self.warnings.append(

            warning

        )


    def add_error(

        self,

        error

    ):

        self.errors.append(

            error

        )


    def clear(self):

        self.warnings.clear()

        self.errors.clear()

        self.status = "Healthy"

        self.message = "System OK"