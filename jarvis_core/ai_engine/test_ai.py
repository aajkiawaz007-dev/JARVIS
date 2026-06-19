from jarvis_core.ai_engine.local_ai import ask_jarvis

while True:

    user = input("\nYOU: ")

    if user.lower() == "exit":
        break

    reply = ask_jarvis(user)

    print("\nJARVIS:", reply)