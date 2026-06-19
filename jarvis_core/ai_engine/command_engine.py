import os
import webbrowser


# ================= EXECUTE COMMAND =================

def execute_command(user_message):

    text = user_message.lower()


    # ================= OPEN NOTEPAD =================

    if "open notepad" in text:

        os.system("start notepad")

        return "Opening Notepad."


    # ================= OPEN CALCULATOR =================

    elif "open calculator" in text:

        os.system("start calc")

        return "Opening Calculator."


    # ================= OPEN CHROME =================

    elif "open chrome" in text:

        os.system(
            "start chrome"
        )

        return "Opening Chrome."


    # ================= OPEN YOUTUBE =================

    elif "open youtube" in text:

        webbrowser.open(

            "https://youtube.com"
        )

        return "Opening YouTube."


    # ================= OPEN GOOGLE =================

    elif "open google" in text:

        webbrowser.open(

            "https://google.com"
        )

        return "Opening Google."


    # ================= OPEN JARVIS CHAT =================

    elif "open ai chat" in text:

        webbrowser.open(

            "http://127.0.0.1:5000/jarvis-chat"
        )

        return "Opening AI Chat."


    # ================= OPEN MUSIC MODULE =================

    elif "open music module" in text:

        webbrowser.open(

            "http://127.0.0.1:5000/music-studio"
        )

        return "Opening Music Studio."


    # ================= SHUTDOWN SYSTEM =================

    elif "shutdown system" in text:

        return (
            "Shutdown command blocked "
            "for safety."
        )


    # ================= RESTART SYSTEM =================

    elif "restart system" in text:

        return (
            "Restart command blocked "
            "for safety."
        )


    # ================= NO COMMAND =================

    return None