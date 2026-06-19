class CommandRouter:
    def route(self, cmd: str) -> str:
        cmd_lower = cmd.lower()

        if "news" in cmd_lower:
            return "news_module"

        if "video" in cmd_lower:
            return "video_module"

        if "upload" in cmd_lower:
            return "automation_module"

        if "case" in cmd_lower or "court" in cmd_lower:
            return "legal_module"

        if "member" in cmd_lower or "ngo" in cmd_lower:
            return "ngo_module"

        return "general"