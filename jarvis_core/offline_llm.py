import subprocess

class OfflineLLM:
    def __init__(self, model_name="phi3"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                text=True,
                capture_output=True
            )

            if result.returncode != 0:
                return f"LLM Error: {result.stderr}"

            return result.stdout.strip()

        except Exception as e:
            return f"Exception in OfflineLLM: {str(e)}"