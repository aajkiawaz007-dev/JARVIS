# =====================================================
# UNIVERSAL AUDIT LOGGER
# =====================================================

import json
import os

from datetime import datetime


AUDIT_FILE = os.path.join(
    os.path.dirname(__file__),
    "audit_log.json"
)


class AuditLogger:

    def __init__(self):

        if not os.path.exists(AUDIT_FILE):

            with open(
                AUDIT_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def write(

        self,

        action,

        status,

        message=""

    ):

        with open(

            AUDIT_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            logs = json.load(file)

        logs.append({

            "time":

                str(

                    datetime.now()

                ),

            "action":

                action,

            "status":

                status,

            "message":

                message

        })

        with open(

            AUDIT_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                logs,

                file,

                indent=4

            )


    def read(self):

        with open(

            AUDIT_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    def clear(self):

        with open(

            AUDIT_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                [],

                file,

                indent=4

            )