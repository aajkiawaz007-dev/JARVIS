from flask import Blueprint, render_template

module_bp = Blueprint(
    "module_bp",
    __name__
)

# ================= MODULE ENGINE =================

def render_module(title, description):

    return render_template(
        "module_page.html",
        title=title,
        description=description
    )

# ================= MODULE ROUTES =================

@module_bp.route("/music-studio")
def music_studio():

    return render_template(
        "jarvis_modules/music_studio/music_studio.html"
    )

@module_bp.route("/video-editor")
def video_editor():

    return render_template(
        "jarvis_modules/video_editor/video_editor.html"
    )

@module_bp.route("/bahujan-party")
def bahujan_party():
    return render_template(
       "jarvis_modules/bahujan_party/bahujan_party.html"
    )

@module_bp.route("/jeene-do-foundation")
def ngo_system():
    return render_template(
        "jarvis_modules/jeene_do_foundation/jeene_do_foundation.html"
    )

@module_bp.route("/msz-system")
def msz_system():
    return render_template(
        "jarvis_modules/msz_system/msz_system.html"
    )

@module_bp.route("/ai-notepad")
def ai_notepad():
    return render_template(
       "jarvis_modules/ai_notepad/ai_notepad.html"
    )

@module_bp.route("/picture-editor")
def picture_editor():
    return render_template(
        "jarvis_modules/picture_editor/picture_editor.html"
    )

@module_bp.route("/id-banner-editor")
def id_banner_editor():
    return render_template(
        "jarvis_modules/id_banner_editor/id_banner_editor.html"
    )

@module_bp.route("/create-picture")
def create_picture():
    return render_template(
        "jarvis_modules/create_picture/create_picture.html"
    )

@module_bp.route("/create-video")
def create_video():
    return render_template(
        "jarvis_modules/create_video/create_video.html"
    )

@module_bp.route("/create-story")
def create_story():
    return render_template(
        "jarvis_modules/create_story/create_story.html"
    )

@module_bp.route("/background-sound")
def background_sound():
    return render_template(
       "jarvis_modules/background_sound/background_sound.html"
    )

@module_bp.route("/ai-english-teacher")
def ai_english_teacher():
    return render_template(
        "jarvis_modules/ai_english_teacher/ai_english_teacher.html"
    )

@module_bp.route("/law-case-handler")
def law_case_handler():
    return render_template(
        "jarvis_modules/law_case_handler/law_case_handler.html"
    )

@module_bp.route("/law-study")
def law_study():
    return render_template(
        "jarvis_modules/law_study/law_study.html"
    )

@module_bp.route("/office-assistant")
def office_assistant():
    return render_template(
        "jarvis_modules/office_assistant/office_assistant.html"
    )

@module_bp.route("/personal-assistant")
def personal_assistant():
    return render_template(
        "jarvis_modules/personal_assistant/personal_assistant.html"
    )

@module_bp.route("/map-assistant")
def map_assistant():
    return render_template(
        "jarvis_modules/map_assistant/map_assistant.html"
    )

@module_bp.route("/video-uploader")
def video_uploader():
    return render_template(
        "jarvis_modules/video_uploader/video_uploader.html"
    )

@module_bp.route("/language-translator")
def language_translator():
    return render_template(
        "jarvis_modules/language_translator/language_translator.html"
    )

@module_bp.route("/game-center")
def game_center():
    return render_template(
       "jarvis_modules/game_center/game_center.html"
    )

@module_bp.route("/drone-assistant")
def drone_assistant():
    return render_template(
        "jarvis_modules/drone_assistant/drone_assistant.html"
    )

@module_bp.route("/home-assistant")
def home_assistant():
    return render_template(
        "jarvis_modules/home_assistant/home_assistant.html"
    )

@module_bp.route("/cleaning-robot")
def cleaning_robot():
    return render_template(
        "jarvis_modules/cleaning_robot/cleaning_robot.html"
    )

@module_bp.route("/weather-assistant")
def weather_assistant():
    return render_template(
        "jarvis_modules/weather_assistant/weather_assistant.html"
    )

@module_bp.route("/app-store")
def app_store():
    return render_template(
        "jarvis_modules/app_store/app_store.html"
    )

@module_bp.route("/ai-core")
def ai_core():
    return render_template(
        "jarvis_modules/ai_core/ai_core.html"
    )

@module_bp.route("/friends-book")
def friends_book():
    return render_template(
        "jarvis_modules/friends_book/friends_book.html"
    )

@module_bp.route("/truster")
def truster():
    return render_template(
        "jarvis_modules/truster/truster.html",
        "Truster",
    )