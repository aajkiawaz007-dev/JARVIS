from datetime import datetime

LOG_FILE = "jarvis_logs/actions.log"

def log_action(action: str):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {action}\n")