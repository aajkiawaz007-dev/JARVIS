def format_memory(rows):
    if not rows:
        return "No previous memory."

    context_text = ""
    for user_text, jarvis_reply, created_at in rows:
        context_text += f"[{created_at}]\nUser: {user_text}\nJarvis: {jarvis_reply}\n\n"

    return context_text.strip()