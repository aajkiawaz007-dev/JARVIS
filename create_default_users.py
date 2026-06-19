from jarvis_database.db_manager import DatabaseManager

db = DatabaseManager()

default_users = [
    ("admin", "admin123", "admin"),
    ("uploader", "upload123", "uploader"),
    ("viewer", "view123", "viewer")
]

for username, password, role in default_users:
    try:
        db.create_user(username, password, role)
        print(f"Created user: {username}")
    except:
        print(f"User already exists: {username}")

print("Default users setup complete.")