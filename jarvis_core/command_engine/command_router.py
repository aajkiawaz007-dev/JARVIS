# =====================================================
# JARVIS OFFLINE COMMAND ROUTER
# =====================================================

def process_command(command):

    command = command.lower()

    # =================================================
    # MUSIC
    # =================================================

    if "music" in command:

        return {
            "reply":
            "Opening Music Studio",

            "module":
            "/music-studio"
        }

    # =================================================
    # GAME
    # =================================================

    elif "game" in command:

        return {
            "reply":
            "Opening Game Center",

            "module":
            "/game-center"
        }

    # =================================================
    # LAW
    # =================================================

    elif "law" in command:

        return {
            "reply":
            "Opening Law Study",

            "module":
            "/law-study"
        }

    # =================================================
    # WEATHER
    # =================================================

    elif "weather" in command:

        return {
            "reply":
            "Opening Weather Assistant",

            "module":
            "/weather-assistant"
        }

    # =================================================
    # UNKNOWN
    # =================================================

    return {

        "reply":
        "Command not found.",

        "module":
        None
    }