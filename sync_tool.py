from pathlib import Path

# ==========================================
# जिस फाइल पर काम करना है उसका नाम
print("1 = README.md")
print("2 = resource.json")
print("3 = config.json")
print("4 = requirements.txt")
print("5 = ROADMAP.md")

choice = input("Select: ").strip()

FILES = {
    "1": "README.md",
    "2": "resource.json",
    "3": "config.json",
    "4": "requirements.txt",
    "5": "ROADMAP.md"
}

TARGET_FILE = FILES[choice]

if TARGET_FILE is None:
    print("Invalid Choice")
    exit()

# नीचे जो टेक्स्ट जोड़ना है वह लिखें
TEXT_TO_APPEND = """

## Phase 7 Extension Step 12

Universal Maintenance Manager

"""
# ==========================================

root = Path(__file__).parent

count = 0

for file in root.rglob(TARGET_FILE):

    # venv, .git, __pycache__ को छोड़ दो
    if any(part in ["venv", ".git", "__pycache__"] for part in file.parts):
        continue

    content = file.read_text(encoding="utf-8")

    if TEXT_TO_APPEND.strip() in content:
        print(f"Skipped : {file}")
        continue

    with open(file, "a", encoding="utf-8") as f:
        f.write(TEXT_TO_APPEND)

    print(f"Updated : {file}")
    count += 1

print(f"\nDone : {count} files updated.")