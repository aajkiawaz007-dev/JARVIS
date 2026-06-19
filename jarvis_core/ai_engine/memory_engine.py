import json
import os

MEMORY_FILE = "jarvis_memory/memory.json"


# ================= LOAD MEMORY =================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:

            json.dump([], file)

    with open(MEMORY_FILE, "r") as file:

        return json.load(file)


# ================= SAVE MEMORY =================

def save_memory(user_message, jarvis_reply):

    memory = load_memory()

    memory.append({

        "user": user_message,

        "jarvis": jarvis_reply
    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(

            memory,

            file,

            indent=4
        )


# ================= GET RECENT MEMORY =================

def get_recent_memory(limit=5):

    memory = load_memory()

    return memory[-limit:]