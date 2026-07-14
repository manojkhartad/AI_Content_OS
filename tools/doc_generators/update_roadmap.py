import json
from pathlib import Path

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

json_file = BASE_DIR / "config" / "roadmap.json"
output_file = BASE_DIR / "docs" / "00_Project" / "ROADMAP.md"

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

# Product Roadmap

Version: {data["version"]}

Status: {data["status"]}

---

# Vision

{data["vision"]}

---

# Development Principles

"""

for item in data["principles"]:
    markdown += f"- {item}\n"

markdown += "\n---\n\n"

for index, stage in enumerate(data["stages"], start=1):

    markdown += f"## Stage {index} — {stage['title']}\n\n"

    markdown += f"Status\n\n"

    if stage["status"] == "Completed":
        markdown += "✅ Completed\n\n"
    else:
        markdown += "🟡 Planned\n\n"

    markdown += f"Goal\n\n{stage['goal']}\n\n"

    markdown += "Components\n\n"

    for component in stage["components"]:
        markdown += f"- {component}\n"

    markdown += "\nOutcome\n\n"

    markdown += stage["outcome"]

    markdown += "\n\n---\n\n"

markdown += f"""# Next Milestone

{data["next_milestone"]}
"""

# ----------------------------------------------------
# Write File
# ----------------------------------------------------

with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown)

print("\nGenerated Markdown:\n")
print(markdown)

print(f"\nCharacters Written: {len(markdown)}")

print("\nROADMAP.md updated successfully.")