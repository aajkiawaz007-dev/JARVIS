from flask import Blueprint, render_template, session, redirect
from jarvis_database.db_manager import DatabaseManager
from jarvis_ui.api_backend.auth.role_required import role_required
from jarvis_core.activity_logger import log_action

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

db = DatabaseManager()

@admin_bp.route("/dashboard")
@role_required("admin")
def dashboard():

    if "role" not in session or session["role"] != "admin":
        return redirect("/login")

    rows = db.get_all_requests()

    requests = []

    for row in rows:
        requests.append({
            "id": row[0],
            "title": row[1],
            "status": row[2],
            "created_by": row[3],
            "created_at": row[4]
        })

    return render_template(
        "admin_dashboard.html",
        requests=requests
    )

@admin_bp.route("/approve/<int:req_id>")
def approve(req_id):

    if "role" not in session or session["role"] != "admin":
        return redirect("/login")

    db.update_request_status(req_id, "approved")

    log_action(f"Admin approved request ID {req_id}")

    return redirect("/admin/dashboard")

@admin_bp.route("/reject/<int:req_id>")
def reject(req_id):

    if "role" not in session or session["role"] != "admin":
        return redirect("/login")

    db.update_request_status(req_id, "rejected")

    log_action(f"Admin rejected request ID {req_id}")

    return redirect("/admin/dashboard")