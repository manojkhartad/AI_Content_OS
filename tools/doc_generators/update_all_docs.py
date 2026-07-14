import subprocess
import sys
from pathlib import Path

# ----------------------------------------------------
# Base Directory
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

generators = [
    "update_project_status.py",
    "update_devlog.py",
    "update_roadmap.py",
    # Future generators
    # "update_architecture.py",
    # "update_decisions.py",
]

print("=" * 60)
print("AI Content OS Documentation Generator")
print("=" * 60)

success = 0
failed = 0

for generator in generators:

    script = BASE_DIR / generator

    print(f"\nRunning: {generator}")

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=BASE_DIR.parent.parent
    )

    if result.returncode == 0:
        print(f"SUCCESS : {generator}")
        success += 1
    else:
        print(f"FAILED  : {generator}")
        failed += 1

print("\n" + "=" * 60)
print("Documentation Generation Finished")
print("=" * 60)

print(f"Successful : {success}")
print(f"Failed     : {failed}")
print(f"Total      : {len(generators)}")

if failed == 0:
    print("\nAll documentation updated successfully.")
else:
    print("\nSome generators failed.")