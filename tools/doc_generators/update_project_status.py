import json
from pathlib import Path

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

metadata_file = BASE_DIR / "config" / "project_metadata.json"
output_file = BASE_DIR / "docs" / "00_Project" / "PROJECT_STATUS.md"

print(f"BASE_DIR      : {BASE_DIR}")
print(f"Metadata File : {metadata_file}")
print(f"Output File   : {output_file}")

# ----------------------------------------------------
# Validate Files
# ----------------------------------------------------

if not metadata_file.exists():
    raise FileNotFoundError(f"Metadata file not found:\n{metadata_file}")

output_file.parent.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------
# Read Metadata
# ----------------------------------------------------

with open(metadata_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# ----------------------------------------------------
# Generate Markdown
# ----------------------------------------------------

markdown = f"""# {data['project_name']}

## Project Information

- **Version:** {data['version']}
- **Phase:** {data['phase']}
- **Current Milestone:** {data['current_milestone']}
- **Next Milestone:** {data['next_milestone']}

---

## Completed Modules

"""

for module in data["completed_modules"]:
    markdown += f"- ✅ {module}\n"

markdown += "\n---\n\n## Pending Modules\n\n"

for module in data["pending_modules"]:
    markdown += f"- ⏳ {module}\n"

# ----------------------------------------------------
# Write Markdown
# ----------------------------------------------------

with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown)
    f.flush()

print("\nGenerated Markdown:\n")
print(markdown)

print(f"\nCharacters Written: {len(markdown)}")
print(f"\nPROJECT_STATUS.md updated successfully.")