from jarvis_core.security import hash_password
import sqlite3
from jarvis_core.config import DB_PATH

class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        self.init_database()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def init_database(self):
        conn = self.connect()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
        """)

        # Upload requests table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS upload_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            status TEXT DEFAULT 'pending',
            created_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    # ---------------- USERS ----------------

    def create_user(self, username, password, role):
        conn = self.connect()
        cursor = conn.cursor()

        hashed = hash_password(password)

        cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, (username, hashed, role))

        conn.commit()
        conn.close()

    def get_user(self, username):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT username, password, role
        FROM users
        WHERE username = ?
        """, (username,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------- UPLOAD REQUESTS ----------------

    def create_upload_request(self, title, created_by):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO upload_requests (title, created_by)
        VALUES (?, ?)
        """, (title, created_by))

        conn.commit()
        conn.close()

    def get_all_requests(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, title, status, created_by, created_at
        FROM upload_requests
        ORDER BY id DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    def update_request_status(self, req_id, status):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE upload_requests
        SET status = ?
        WHERE id = ?
        """, (status, req_id))

        conn.commit()
        conn.close()