from flask import Blueprint, render_template, request, redirect, session
from jarvis_core.security import verify_password
from jarvis_database.db_manager import DatabaseManager

auth_bp = Blueprint("auth", __name__)

db = DatabaseManager()

@auth_bp.route("/")
def home():
    return redirect("/login")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = db.get_user(username)

        if user:
            db_username, db_password, db_role = user

            if verify_password(db_password, password):
                session["user"] = db_username
                session["role"] = db_role

                if db_role == "admin":
                    return redirect("/admin/dashboard")

                return redirect("/user/dashboard")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")