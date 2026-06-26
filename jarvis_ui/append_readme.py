from pathlib import Path

TEXT = """

--------------------------------------------------
## 🚀 New Update

यह टेक्स्ट सभी README.md के अंत में जोड़ा जाएगा।

"""

root = Path(__file__).parent

count = 0

for readme in root.rglob("README.md"):
    content = readme.read_text(encoding="utf-8")

    # अगर टेक्स्ट पहले से है तो छोड़ दो
    if TEXT.strip() in content:
        print(f"Skipped: {readme}")
        continue

    with open(readme, "a", encoding="utf-8") as f:
        f.write(TEXT)

    print(f"Updated: {readme}")
    count += 1

print(f"\nDone! {count} README.md files updated.")