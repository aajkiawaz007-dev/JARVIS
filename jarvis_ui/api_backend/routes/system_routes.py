from flask import Blueprint, jsonify
import psutil
import platform
from datetime import datetime

system_bp = Blueprint(
    "system_bp",
    __name__
)

@system_bp.route("/system-status")
def system_status():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    return jsonify({

        "cpu": cpu,
        "ram": ram,
        "time": datetime.now().strftime("%H:%M:%S"),

        "system": platform.system(),

        "status": "JARVIS ACTIVE"
    })