from transformers import pipeline

from jarvis_core.ai_engine.command_engine import (
    execute_command
)

from jarvis_core.ai_engine.memory_engine import (
    save_memory,
    get_recent_memory
)

print("Loading JARVIS Offline Brain...")

chatbot = pipeline(

    "text-generation",

    model="distilgpt2"
)

print("JARVIS Brain Loaded")


def ask_jarvis(user_message):

    try:

                # ================= COMMAND ENGINE =================

        command_result = execute_command(
            user_message
        )

        if command_result:

            save_memory(

                user_message,

                command_result
            )

            return command_result

        # ================= LOAD MEMORY =================

        recent_memory = get_recent_memory()

        memory_context = ""

        for chat in recent_memory:

            memory_context += (

                f"User: {chat['user']}\n"

                f"Jarvis: {chat['jarvis']}\n"
            )

        # ================= FULL PROMPT =================

        full_prompt = (

            memory_context +

            f"\nUser: {user_message}\n"

            f"Jarvis:"
        )

        # ================= AI RESPONSE =================

        response = chatbot(

            full_prompt,

            max_length=120,

            num_return_sequences=1
        )

        answer = response[0]["generated_text"]

        # ================= SAVE MEMORY =================

        save_memory(

            user_message,

            answer
        )

        return answer

    except Exception as error:

        return f"AI ERROR: {error}"