import json
from pathlib import Path

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

json_file = BASE_DIR / "config" / "devlog.json"
output_file = BASE_DIR / "docs" / "00_Project" / "DEVLOG.md"

print(f"BASE_DIR    : {BASE_DIR}")
print(f"JSON File   : {json_file}")
print(f"Output File : {output_file}")

# ----------------------------------------------------
# Read JSON
# ----------------------------------------------------

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# ----------------------------------------------------
# Generate Markdown
# ----------------------------------------------------

markdown = f"""# {data["project_name"]}

# Development Log

Version: {data["version"]}

Status: {data["status"]}

---

"""

for i, phase in enumerate(data["phases"], start=1):

    markdown += f"## Phase {i} — {phase['title']}\n\n"

    markdown += f"Status\n\n"

    if phase["status"] == "Completed":
        markdown += "✅ Completed\n\n"
    else:
        markdown += f"{phase['status']}\n\n"

    markdown += "Work Completed\n\n"

    for item in phase["work_completed"]:
        markdown += f"- {item}\n"

    markdown += "\nOutcome\n\n"

    markdown += phase["outcome"]

    markdown += "\n\n---\n\n"

markdown += f"""# Next Development Target

{data["next_target"]}
"""

# ----------------------------------------------------
# Write File
# ----------------------------------------------------

with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown)

print("\nGenerated Markdown:\n")
print(markdown)

print(f"\nCharacters Written: {len(markdown)}")

print("\nDEVLOG.md updated successfully.")