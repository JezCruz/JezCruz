from datetime import datetime, timezone

START = "<!--START_SECTION:dev-->"
END = "<!--END_SECTION:dev-->"

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

new_content = f"""Last update: {now}

🚀 Main Project: Skillvine
🟢 Status: Active Development
🛠️ Focus: Django API + Expo Mobile App
📚 Learning: Full-stack development, deployment, and DevOps
"""

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

if START not in readme or END not in readme:
    raise Exception("START_SECTION or END_SECTION marker not found in README.md")

before = readme.split(START)[0]
after = readme.split(END)[1]

updated_readme = before + START + "\n" + new_content + "\n" + END + after

with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("README updated successfully.")
