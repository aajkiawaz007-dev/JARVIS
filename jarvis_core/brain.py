from rich import print
from jarvis_core.memory import JarvisMemory
from jarvis_core.command_router import CommandRouter
from jarvis_core.offline_llm import OfflineLLM
from jarvis_core.prompt_engine import PromptEngine
from jarvis_core.memory_context import format_memory

class JarvisBrain:
    def __init__(self):
        self.name = "JARVIS"
        self.memory = JarvisMemory()
        self.router = CommandRouter()
        self.llm = OfflineLLM(model_name="phi3")
        self.prompt_engine = PromptEngine()

    def start(self):
        print("[bold green]JARVIS Offline System Started[/bold green]")
        print("Commands: exit | memory | clear\n")

        while True:
            cmd = input("You: ").strip()

            if cmd.lower() == "exit":
                print("[bold red]JARVIS shutting down...[/bold red]")
                break

            if cmd.lower() == "memory":
                self.show_memory()
                continue

            if cmd.lower() == "clear":
                print("[yellow]Screen cleared (manual).[/yellow]")
                continue

            self.process_command(cmd)

    def show_memory(self):
        print("[bold yellow]Last Conversations:[/bold yellow]")
        rows = self.memory.get_last_conversations(limit=5)

        if not rows:
            print("[red]No memory found yet.[/red]")
            return

        for user_text, jarvis_reply, created_at in rows:
            print(f"[cyan]{created_at}[/cyan]")
            print(f"[white]You:[/white] {user_text}")
            print(f"[green]Jarvis:[/green] {jarvis_reply}")
            print("-----")

    def process_command(self, cmd: str):
        module = self.router.route(cmd)

        # Load last 5 conversations for context
        last_rows = self.memory.get_last_conversations(limit=5)
        memory_context = format_memory(last_rows)

        prompt = self.prompt_engine.build_prompt(
            user_text=cmd,
            memory_context=memory_context,
            module=module
        )

        reply = self.llm.generate(prompt)

        print(f"[cyan]JARVIS:[/cyan] {reply}")
        self.memory.save_conversation(cmd, reply)