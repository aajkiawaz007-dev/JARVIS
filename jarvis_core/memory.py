import sqlite3
from jarvis_core.config import DB_PATH

class JarvisMemory:
    def __init__(self):
        self.db_path = DB_PATH
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT NOT NULL,
            jarvis_reply TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    def save_conversation(self, user_text: str, jarvis_reply: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO conversations (user_text, jarvis_reply)
        VALUES (?, ?)
        """, (user_text, jarvis_reply))

        conn.commit()
        conn.close()

    def get_last_conversations(self, limit=5):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT user_text, jarvis_reply, created_at
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()
        return rows