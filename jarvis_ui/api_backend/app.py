from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_from_directory
)


from jarvis_core.ai_engine.local_ai import (
    ask_jarvis
)

import os
import psutil
import datetime

from jarvis_ui.api_backend.routes.system_routes import system_bp
from jarvis_ui.api_backend.routes.main_hub_routes import main_hub_bp
from jarvis_ui.api_backend.routes.auth_routes import auth_bp
from jarvis_ui.api_backend.routes.admin_routes import admin_bp
from jarvis_ui.api_backend.routes.user_routes import user_bp
from jarvis_ui.api_backend.routes.module_routes import module_bp


# =====================================================
# CREATE APP
# =====================================================

def create_app():

    app = Flask(
        __name__,
        template_folder="../templates"
    )

    # =====================================================
    # UPLOAD FOLDER
    # =====================================================

    UPLOAD_FOLDER = os.path.join(
        os.getcwd(),
        "uploads",
        "videos"
    )

    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    # =====================================================
    # BLUEPRINTS
    # =====================================================

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(main_hub_bp)
    app.register_blueprint(module_bp)
    app.register_blueprint(system_bp)

    # =====================================================
    # VIDEO ACCESS ROUTE
    # =====================================================

    @app.route('/uploads/videos/<filename>')
    def uploaded_file(filename):

        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename
        )

    # =====================================================
    # LIVE SYSTEM STATUS
    # =====================================================

    @app.route("/live-system-status")
    def live_system_status():

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        battery = psutil.sensors_battery()

        battery_percent = (
            battery.percent
            if battery else 0
        )

        current_time = datetime.datetime.now().strftime(
            "%I:%M:%S %p"
        )

        return jsonify({

            "cpu": cpu,

            "ram": ram,

            "battery": battery_percent,

            "time": current_time,

            "status":
            "JARVIS AI ACTIVE"
        })

    # =====================================================
    # JARVIS MAIN UI
    # =====================================================

    @app.route("/jarvis")
    def jarvis_home():

        return render_template(
            "jarvis_main_hub.html"
        )

    # =====================================================
    # JARVIS CHAT PAGE
    # =====================================================

    @app.route("/jarvis-chat")
    def jarvis_chat():

        return render_template(
            "jarvis_chat.html"
        )

    # =====================================================
    # ASK JARVIS API
    # =====================================================

    @app.route(
        "/ask-jarvis",
        methods=["POST"]
    )
    def ask_jarvis_api():

        data = request.json

        user_message = data.get(
            "message"
        )

        reply = ask_jarvis(
            user_message
        )

        return jsonify({

            "reply": reply
        })

    # =====================================================
    # MAIN AI BACKEND
    # =====================================================

    @app.route(
        "/jarvis-ai",
        methods=["POST"]
    )
    def jarvis_ai():

        data = request.get_json()

        user_message = data.get(
            "message",
            ""
        ).lower()

        # =====================================================
        # BASIC COMMANDS
        # =====================================================
 
        
        if "hello" in user_message:

            reply = "Hello sir. JARVIS online."

        elif "music" in user_message:

            reply = "Opening music module."

        elif "game" in user_message:

            reply = "Opening game center."

        elif "law" in user_message:

            reply = "Opening law study module."

        elif "weather" in user_message:

            reply = "Opening weather assistant."

        else:

            # =====================================================
            # LOCAL AI ENGINE
            # =====================================================

            reply = ask_jarvis(
                user_message
            )

        return jsonify({

            "reply": reply
        })

    return app


# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":

    app = create_app()

    app.run(
        debug=True,
    )