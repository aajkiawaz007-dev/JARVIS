from flask import Blueprint, render_template, session, redirect, request
from jarvis_database.db_manager import DatabaseManager
from jarvis_core.activity_logger import log_action



user_bp = Blueprint("user", __name__, url_prefix="/user")

db = DatabaseManager()

@user_bp.route("/dashboard")
def dashboard():

    if "role" not in session:
        return redirect("/login")

    return render_template(
        "user_dashboard.html",
        role=session["role"]
    )

@user_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if "role" not in session:
        return redirect("/login")

    if session["role"] not in ["uploader", "admin"]:
        return redirect("/user/dashboard")

    if request.method == "POST":

        title = request.form.get("title")

        db.create_upload_request(
            title=title,
            created_by=session["user"]
        )

        log_action(f"{session['user']} created upload request: {title}")

        return render_template(
            "upload.html",
            msg=f"Upload Request Sent for Approval: {title}"
        )

    return render_template("upload.html")