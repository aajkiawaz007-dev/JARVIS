import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "jarvis_database", "jarvis.db")

JARVIS_NAME = "JARVIS"
VERSION = "1.0"