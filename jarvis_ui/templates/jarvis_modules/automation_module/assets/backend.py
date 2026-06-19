from config import (
    MODULE_NAME,
    VERSION,
    STATUS,
    HEALTH
)

def module_health():

    return {

        "module": MODULE_NAME,

        "version": VERSION,

        "status": STATUS,

        "health": HEALTH
    }