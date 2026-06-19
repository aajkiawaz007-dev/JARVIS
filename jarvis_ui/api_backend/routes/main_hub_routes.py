from flask import Blueprint, render_template  # type: ignore[import]

main_hub_bp = Blueprint(
    "main_hub",
    __name__
)

@main_hub_bp.route("/jarvis")
def jarvis_home():
    return render_template("jarvis_main_hub.html")